from django.shortcuts import render
from rest_framework import generics, permissions
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import IdentityListLiteSerializerEN
from .models import (
    Identity,
    Passive,
    Sinner,
    PanicType,
    Skill,
    EnSkillEffect,
    EnCoinEffectList,
    EnCoinEffectDesc,
    SkillData,
    RelPassive,
    RelSkill,
    AttributeCondition,
    EnPassiveDescription,
    CoinList,
    EnIdentityInfo,
    Hp,
    AttackResistList,
    ENStoryChaptersModel
)  # Create your views here.


class IdentityListLite(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = EnIdentityInfo.objects.values("title", "name", "identity")
    serializer_class = IdentityListLiteSerializerEN

def duplicate_along_uptie_level(dict, max_uptie_level):
    temp_dict = dict.copy()
    for skill_id, effects in temp_dict.items():
        # Step 1: Extract the existing levels and find the full range of levels.
        existing_levels = {}
        min_level = 100000000000000000000000000
        max_level = max_uptie_level
        for effect in effects:
            existing_levels[effect["uptie_level"]] = effect
            min_level = min(min_level, effect["uptie_level"])
            max_level = max(max_level, effect["uptie_level"])

        # Step 2: Identify missing levels.
        full_range = list(range(min_level, max_level + 1))
        # Step 3: Fill in the missing levels.
        filled_effects = []
        previous_effect = None
        for level in full_range:
            if level in existing_levels:
                # If level exists, use the existing effect.
                current_effect = existing_levels[level]
            else:
                # If level is missing, use the previous effect's value.
                current_effect = previous_effect.copy()
                current_effect["uptie_level"] = level

            filled_effects.append(current_effect)
            previous_effect = current_effect

        # Step 4: Update the dictionary with the filled effects.
        temp_dict[skill_id] = filled_effects
    return temp_dict


def get_coin_info_for_skill_effect(skill_effect_id):
    coin_dict = {}
    coins = EnCoinEffectList.objects.filter(skill_coin_effect=skill_effect_id).values(
        "action_index", "id"
    )
    for coin in coins:
        coin_descs = EnCoinEffectDesc.objects.filter(coin=coin["id"]).values(
            "desc", "summary"
        )
        coin["descs"] = []
        for descs in coin_descs:
            coin["descs"].append(descs["desc"])
    return list(coins)


def get_coin_info_for_skill_data(skill_datas_id):
    coins = CoinList.objects.filter(skill_data=skill_datas_id).values(
        "operator_type", "scale", "action_index"
    )
    coins = list(coins)
    return sorted(coins, key=lambda d: d["action_index"])


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def IdentityGet(request, pk):
    if request.user.username != "Malcute" and request.user.username != "Aeon":
        return HttpResponse("You are not authorized to access this resource.")
    identity = Identity.objects.get(pk=pk)
    en_info = EnIdentityInfo.objects.get(identity=pk)
    # 1000104 is skill on panic
    skills = (
        RelSkill.objects.exclude(skill=1000104)
        .filter(identity=identity)
        .values("skill", "skill_num")
    )
    # list of skill for querying
    skill_list = [x["skill"] for x in skills]

    ####### Skill Effects ###### DONE
    skill_effect_dict = {}

    skill_effects = EnSkillEffect.objects.filter(skill__in=skill_list).values(
        "id", "skill", "name", "uptie_level", "desc", "keywords"
    )
    for x in skill_effects:
        # skill_dict = {'skill_1':{},'skill_2':{},'skill_3':{},'skill_4':{}}# etc
        skill_effect_dict[x["skill"]] = skill_effect_dict.get(x["skill"], []) + [x]
        # skill_effect_dict[x['skill']]['coinList']
    skill_effect_dict = duplicate_along_uptie_level(skill_effect_dict, 4)
    for skill, effects in skill_effect_dict.items():
        for uptie_level in effects:
            uptie_level["coin_descs"] = get_coin_info_for_skill_effect(
                uptie_level["id"]
            )

    ###############

    ##### Skill Rolls and Attributes ##########
    skill_data_list = {}
    skill_datas = SkillData.objects.filter(skill__in=skill_list).values(
        "skill",
        "uptie_level",
        "attribute_type",
        "atk_type",
        "def_type",
        "skill_target_type",
        "target_num",
        "mp_usage",
        "default_value",
        "id",
        "icon_id",
    )
    for x in skill_datas:
        # skill_dict = {'skill_1':{},'skill_2':{},'skill_3':{},'skill_4':{}}# etc
        skill_data_list[x["skill"]] = skill_data_list.get(x["skill"], []) + [x]

    skill_data_list = duplicate_along_uptie_level(skill_data_list, 4)
    for coin, skill_data in skill_data_list.items():
        coin_roll = []
        for skill in skill_data:
            new_coin_roll = get_coin_info_for_skill_data(skill["id"])
            if len(new_coin_roll) != 0:
                skill["coin_roll"] = new_coin_roll
                coin_roll = new_coin_roll
            else:
                skill["coin_roll"] = coin_roll

    ##########

    ##### Passives ##########
    passive_data = list(
        RelPassive.objects.filter(identity=pk).values(
            "passive", "uptie_level", "is_support"
        )
    )
    passive_data = [ passive for passive in passive_data if EnPassiveDescription.objects.filter(passive=passive["passive"]).exists()]
    for passive in passive_data:
        try:
            passive["attribution"] = list(
                map(
                    model_to_dict,
                    AttributeCondition.objects.filter(passive=passive["passive"]),
                )
            )
        except:
            passive["attribution"] = []
        curr_passive = EnPassiveDescription.objects.filter(passive=passive["passive"])
        passive["ENDescription"] = model_to_dict(curr_passive[0])

    ###############

    final_dict = {}
    final_dict["skill_effect"] = skill_effect_dict
    final_dict["skill_data"] = skill_data_list
    final_dict["passives"] = passive_data
    final_dict["characterId"] = identity.characterId.name
    final_dict["panicType"] = identity.panicType.panicName
    final_dict["rarity"] = identity.rank
    final_dict["defCorrection"] = identity.defCorrection
    final_dict["minSpeedList"] = identity.minSpeedList
    final_dict["maxSpeedList"] = identity.maxSpeedList
    final_dict["uniqueAttribute"] = identity.uniqueAttribute
    final_dict["breakSection"] = identity.breakSection
    final_dict["HP"] = model_to_dict(Hp.objects.get(id=pk))
    final_dict["name"] = en_info.title
    final_dict["sinner"] = str(identity.characterId.name)
    final_dict["attack_resist"] = list(
        AttackResistList.objects.filter(identity=pk).values("atk_type", "value")
    )
    final_dict["id"] = identity.id
    skill_temp = {}
    for s in skills:
        skill_temp[s["skill"]] = s["skill_num"]
    final_dict["skill_num"] = skill_temp
    return JsonResponse(final_dict)


import random
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def Gacha(request):
    gacha_pool_iden = EnIdentityInfo.objects.select_related("identity").values("identity__rank", "nameWithTitle", "title", "identity_id")
    gacha_pool_ego = EnEgoInfo.objects.select_related("ego").values("ego__id", "name")
    
    SPECIAL = 13
    EGO_CHANCE = 13
    IDENTITY_000_CHANCE = 29
    IDENTITY_00_CHANCE = 128
    IDENTITY_0_CHANCE = 817
    TOTAL = 1000
    
    results = []
    
    for _ in range(10):
        roll = random.randint(1, TOTAL)
        
        if roll <= SPECIAL:
            results.append({"id": None, "name": "Special Item", "rank": "Special"})
        elif roll <= SPECIAL + EGO_CHANCE:
            chosen = random.choice(list(gacha_pool_ego))
            results.append({"id": chosen['ego__id'], "name": chosen['name'], "rank": "Ego"})
        elif roll <= SPECIAL + EGO_CHANCE + IDENTITY_000_CHANCE:
            chosen = random.choice([iden for iden in gacha_pool_iden if iden['identity__rank'] == 3])
            results.append({"id": chosen['identity_id'], "name": chosen['nameWithTitle'], "alt_name": chosen['title'], "rank": 3})
        elif roll <= SPECIAL + EGO_CHANCE + IDENTITY_000_CHANCE + IDENTITY_00_CHANCE:
            chosen = random.choice([iden for iden in gacha_pool_iden if iden['identity__rank'] == 2])
            results.append({"id": chosen['identity_id'], "name": chosen['nameWithTitle'], "alt_name": chosen['title'], "rank": 2})
        else:
            chosen = random.choice([iden for iden in gacha_pool_iden if iden['identity__rank'] == 1])
            results.append({"id": chosen['identity_id'], "name": chosen['nameWithTitle'], "alt_name": chosen['title'], "rank": 1})
    
    return JsonResponse(results, safe=False)




from .models import (
    EgoSkill,
    EgoSkillData,
    EgoCoinList,
    EnEgoSkillEffect,
    EnEgoSkillCoinEffect,
    EnEgoSkillCoinEffectDesc,
    Ego,
    EnEgoInfo,
    EgoAttributeResist,
    EgoRequirement,
    EgoCorrosionSection,
    EgoPassive,
    EnEgoPassive,
    RelPassiveEGO,
)

def ego_coin_list_analysis(ego_skill_data):
    coin_lists = sorted(
        list(
            EgoCoinList.objects.filter(ego_skill_data=ego_skill_data).values(
                "operator_type", "scale", "action_index", "id"
            )
        ),
        key=lambda x: x["action_index"],
    )
    return coin_lists


def ego_coin_effect_list_analysis(skill_effect_id):
    coin_effect_list = list(
        EnEgoSkillCoinEffect.objects.filter(ego_skill_effect=skill_effect_id)
        .order_by("action_index")
        .values("id", "action_index")
    )
    for i in coin_effect_list:
        coin_list = []
        coin_descs = list(
            EnEgoSkillCoinEffectDesc.objects.filter(
                ego_skill_coin_effect=i["id"]
            ).values("desc")
        )
        for descs in coin_descs:
            coin_list.append(descs["desc"])
        i["descs"] = coin_list
    return coin_effect_list


def ego_skill_analysis(ego_skill, max_uptie_level=4):
    skill_data = list(
        EgoSkillData.objects.filter(ego_skill=ego_skill)
        .order_by("uptie_level")
        .values(
            "id",
            "uptie_level",
            "attribute_type",
            "atk_type",
            "def_type",
            "skill_target_type",
            "target_num",
            "mp_usage",
            "skill_level_correction",
            "default_value",
            "can_team_kill",
            "can_duel",
            "can_change_target",
            "skill_motion",
            "view_type",
            "parrying_close_type",
            "icon_id",
        )
    )
    min_uptie_level = skill_data[0]["uptie_level"]
    filled_effects = []
    previous_effect = None
    previous_roll = None
    existing_levels = {}
    for x in skill_data:
        existing_levels[int(x["uptie_level"])] = x
    for uptie_index in range(min_uptie_level, max_uptie_level + 1):
        # Step 3: Fill in the missing levels.
        if uptie_index in existing_levels:
            # If level exists, use the existing effect.
            current_effect = existing_levels[uptie_index]
            current_effect["coin_roll"] = ego_coin_list_analysis(
                existing_levels[uptie_index]["id"]
            )
            if len(current_effect["coin_roll"]) < 1:
                current_effect["coin_roll"] = previous_roll
        else:
            # If level is missing, use the previous effect's value.
            current_effect = previous_effect.copy()
            current_effect["uptie_level"] = uptie_index

        filled_effects.append(current_effect)
        previous_roll = current_effect["coin_roll"]
        previous_effect = current_effect

        # Step 4: Update the dictionary with the filled effects.
    sorted(filled_effects, key=lambda x: x["uptie_level"])
    return filled_effects


def ego_skill_effect_analysis(ego_skill, max_uptie_level=4):
    skill_effect = list(
        EnEgoSkillEffect.objects.filter(ego_skill=ego_skill)
        .order_by("uptie_level")
        .values("id", "name", "desc", "uptie_level")
    )
    for effect in skill_effect:
        effect["coin_descs"] = ego_coin_effect_list_analysis(effect["id"])
    min_uptie_level = skill_effect[0]["uptie_level"]
    filled_effects = []
    previous_effect = None
    existing_levels = {}
    for x in skill_effect:
        existing_levels[int(x["uptie_level"])] = x

    for uptie_index in range(min_uptie_level, max_uptie_level + 1):
        # Step 3: Fill in the missing levels.
        if uptie_index in existing_levels:
            # If level exists, use the existing effect.
            current_effect = existing_levels[uptie_index]
        else:
            # If level is missing, use the previous effect's value.
            current_effect = previous_effect.copy()
            current_effect["uptie_level"] = uptie_index

        filled_effects.append(current_effect)
        previous_effect = current_effect

        # Step 4: Update the dictionary with the filled effects.
    sorted(filled_effects, key=lambda x: x["uptie_level"])
    return filled_effects


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def EgoGet(request, pk):
    ego = Ego.objects.get(pk=pk)
    ego_dict = {}
    EN_ego_info = model_to_dict(EnEgoInfo.objects.get(ego=pk))
    awakeningSkill = ego.awakeningSkillId
    corrosionSkill = ego.corrosionSkillId
    ego_dict["awakeningSkill"] = ego_skill_analysis(awakeningSkill.pk)
    ego_dict["awakeningSkillEffect"] = ego_skill_effect_analysis(awakeningSkill.pk)
    if corrosionSkill:
        ego_dict["corrosionSkill"] = ego_skill_analysis(corrosionSkill.pk)
        ego_dict["corrosionSkillEffect"] = ego_skill_effect_analysis(corrosionSkill.pk)

    ego_dict["id"] = ego.id
    ego_dict["characterId"] = ego.characterId.name
    ego_dict["egoType"] = ego.egoType
    ego_dict["egoClass"] = ego.egoClass
    ego_dict["season"] = ego.season
    ego_dict["skilltier"] = ego.skilltier
    ego_dict["additionalAttachment"] = ego.additionalAttachment
    ego_dict["walpurgisType"] = ego.walpurgisType
    ego_dict["passive"] = []
    ego_dict["en_info"] = EN_ego_info
    ego_dict["attribute_resist"] = list(
        EgoAttributeResist.objects.filter(ego=pk).values("type", "value")
    )
    ego_dict["requirement"] = list(
        EgoRequirement.objects.filter(ego=pk).values("attributeType", "num")
    )

    for i in ego.passive.all():
        temp_passive = {}
        all_en_passives = EnEgoPassive.objects.get(ego_passive=i.id)
        temp_passive["name"] = all_en_passives.name
        temp_passive["desc"] = all_en_passives.desc
        ego_dict["passive"].append(temp_passive.copy())

    return JsonResponse(ego_dict)


from django.contrib.postgres.search import TrigramSimilarity
from .models import (EnLimbusStory,ModelToChar,StoryTheater,StoryTheaterList,EnStageChapter,EnStageNode)
from .serializers import EnLimbusStorySerializer
from rest_framework.views import APIView
from random import choice

def story_fill(EN_limbus_story : EnLimbusStory):
    node_id = EN_limbus_story.theater_story_id.node_id
    chapter_id = EN_limbus_story.theater_story_id.story_theater.id
    stage_info = EnStageNode.objects.filter(id=node_id)
    chapter_info = EnStageChapter.objects.filter(id_int=chapter_id)
    data = dict(EnLimbusStorySerializer(EN_limbus_story).data)
    data["chapter_info"] = None
    data["stage_id"] = None
    data["stage_info"] = None
    data["stage_place"] = None
    if data.get("model"):
        model_data = list(ModelToChar.objects.filter(id=data["model"]).values("enname","enNickName","id"))
        if len(model_data) > 0:
            data["model"] = model_data[0]
    if len(chapter_info)>0:
        data["chapter_info"] = str(chapter_info[0])
    if len(stage_info)>0:
        data["stage_info"] = stage_info[0].title
        data["stage_id"] = EN_limbus_story.theater_story_id.id_index
        data["stage_place"] = stage_info[0].place
    return json.dumps(data,ensure_ascii=False)

class StoryAcquire(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self,request,format=None):
        if request.user.username != "Malcute":
            return Response("None")  
        data = request.data.copy()
        string_param = data.get("search","")
        filtered_data = EnLimbusStory.objects.filter(content__icontains=string_param)
        if len(filtered_data) > 0:
            results = (
                filtered_data.annotate(
                    similarity=TrigramSimilarity("content", string_param)
                )
                .filter(similarity__gt=0.3)
                .order_by("-similarity")
            )
        else:
            results = (
                EnLimbusStory.objects.annotate(
                    similarity=TrigramSimilarity("content", string_param)
                )
                .filter(similarity__gt=0.3)
                .order_by("-similarity")
            )
        if len(results) == 0:
            return Response("No Data Found")

        primary_result = results[0]
        return Response(story_fill(primary_result))

class StoryAcquireList(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request,format=None):
        # if request.user.username != "Malcute":
        #     return Response("None")  
        data = request.data.copy()
        string_param = data.get("search","")
        filtered_data = EnLimbusStory.objects.filter(content__icontains=string_param)
        if len(filtered_data) > 0:
            results = (
                filtered_data.annotate(
                    similarity=TrigramSimilarity("content", string_param)
                )
                .filter(similarity__gt=0.3)
                .order_by("-similarity")
            )
        else:
            results = (
                EnLimbusStory.objects.annotate(
                    similarity=TrigramSimilarity("content", string_param)
                )
                .filter(similarity__gt=0.3)
                .order_by("-similarity")
            )
        if len(results) == 0:
            return Response("No Data Found")

        final_list = []
        print(results)
        for i in results:
            final_list.append(story_fill(i))
        return Response(final_list)
    

class StoryRandom(APIView):
    def get(self,request):
        pks = EnLimbusStory.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        random_obj = EnLimbusStory.objects.get(pk=random_pk)
        return story_fill(random_obj)


class ENStoryByChapterAndNode(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    def post(self,request,format=None):
        # if request.user.username != "Malcute":
        #     return Response("None")
        try:
            data = request.data.copy()
            chapter = data.get("chapter",None)
            node_data = data.get("id_index",None)
            text_num = data.get("id_raw",None)
            node_id = data.get("node_id",None)
            node_index = data.get("node_index",None)
            if data.get("language",None) == "EN" or data.get("language",None) == None:
                if node_id:
                    node_datas = StoryTheaterList.objects.filter(node_id=node_id,id_index=node_index)
                    if len(node_datas) < 1:
                        return Response("Can't locate node.")
                    node = node_datas[0]
                else:
                    node_datas = StoryTheaterList.objects.filter(story_theater=chapter,id_index=node_data)
                    if len(node_datas) < 1:
                        return Response("Can't locate node. Is the chapter or node number wrong?")
                    node = node_datas[0]
                EN_story = EnLimbusStory.objects.filter(theater_story_id=node.id).order_by("id_raw")
                if len(EN_story) < 1:
                    return Response("Can't locate text. Node and chapter located.")
                story_list = []
                place = None
                for i in EN_story:
                    data_to_add = model_to_dict(i)
                    if data_to_add.get("place") == None:
                        data_to_add["place"] = place
                    else:
                        data_to_add["place"] = data_to_add.get("place")
                        place = data_to_add.get("place")
                    if data_to_add.get("model"):
                        model_data = list(ModelToChar.objects.filter(id=data_to_add["model"]).values("enname","enNickName","id"))
                        if len(model_data) > 0:
                            data_to_add["model"] = model_data[0]
                    story_list.append(data_to_add)
                return Response(story_list)
            else:
                return Response("Not Implemented")
        except:
            return Response("Input error")

class ENChapterNodeList(APIView):
    def get(self,request):
        query = """SELECT 1 as id, h.title, h."chapterNumber",h."stageDetail", h.chaptertitle, h.chapter,h.id_index AS node_index, h.node_id as story_theather_list_node_id
FROM (( 
    SELECT *
    FROM public.limbus2_storytheater AS b
    RIGHT JOIN public.limbus2_enstagechapter AS d
    ON b.id = d.id_int
) AS e
RIGHT JOIN (
    public.limbus2_storytheaterlist AS lst
    LEFT JOIN public.limbus2_enstagenode AS node
    ON lst.node_id = node.id
) AS f
ON e.id_int = f.story_theater_id) AS h
        """
        results = ENStoryChaptersModel.objects.raw(raw_query=query)
        results =[ model_to_dict(r) for r in results]
        return Response(results)

class StoryTheaterGet(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request,format=None):
        data = list(EnStageChapter.objects.all().values())
        return Response(data)

from django.shortcuts import render
from .forms import JSONUploadForm
import json
from .utils import modelmap, natural_key, foreign_key_map

# ✅ Upload View (no cache)
@permission_classes([IsAuthenticated])
def upload_json_view(request):
    if request.user.username != "Aeon":
        return None

    if request.method != 'POST':
        return render(request, 'upload_form.html', {'form': JSONUploadForm()})

    form = JSONUploadForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'upload_form.html', {'form': form})

    files = sorted(request.FILES.getlist('files'), key=natural_key)
    results = []

    for file in files:
        filename = file.name
        model = modelmap.get(filename)
        if not model:
            results.append((filename, 'Unknown model'))
            continue

        try:
            data = json.load(file)
            fks = foreign_key_map.get(filename, {})

            for entry in data:
                obj_id = entry.get('id')
                if obj_id is None:
                    results.append((filename, 'Missing "id" in entry'))
                    continue

                defaults = {k: v for k, v in entry.items() if k != 'id'}

                # 🔄 Resolve foreign keys on the fly
                for field, related_model in fks.items():
                    fk_id = entry.get(field)
                    if fk_id is not None:
                        try:
                            defaults[field] = related_model.objects.get(id=fk_id)
                        except related_model.DoesNotExist:
                            results.append((filename, f'{related_model.__name__} with id {fk_id} not found'))
                            break  # Skip this entry
                else:
                    model.objects.update_or_create(id=obj_id, defaults=defaults)

            results.append((filename, 'Success'))

        except Exception as e:
            results.append((filename, f'Error: {e}'))

    return render(request, 'upload_result.html', {'results': results})


# @permission_classes([IsAuthenticated])
# def upload_json_view(request):
#     if request.user.username == "Aeon":
#         if request.method == 'POST':
#             form = JSONUploadForm(request.POST, request.FILES)
#             if form.is_valid():
#                 files = request.FILES.getlist('files')
#                 files = sorted(files, key=natural_key)
#                 results = []
#                 for file in files:
#                     filename = file.name
#                     model = modelmap.get(filename)
#                     if not model:
#                         results.append((filename, 'Unknown model'))
#                         continue
#                     try:
#                         data = json.load(file)
#                         for entry in data:
#                             obj_id = entry.get('id')
#                             if obj_id is None:
#                                 results.append((filename, 'Missing "id" in entry'))
#                                 continue
#                             # Ensure we preserve the ID and update or create the object
#                             defaults = {k: v for k, v in entry.items() if k != 'id'}
#                             model.objects.update_or_create(id=obj_id, defaults=defaults)
#                         results.append((filename, 'Success'))
#                     except Exception as e:
#                         results.append((filename, f'Error: {e}'))

#                 return render(request, 'upload_result.html', {'results': results})
#         else:
#             form = JSONUploadForm()
#         return render(request, 'upload_form.html', {'form': form})
    
