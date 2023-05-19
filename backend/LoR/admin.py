from django.contrib import admin
from .models import (
    Card,
    Office,
    Rank,
    Deck,
    Page,
    Character,
    RelDeck,
    Guide,
    Effects,
    RelGuide,
    AbnoCards,
)

# admin registers allows databases to be edited from the admin page
admin.site.register(Office)
admin.site.register(Rank)
admin.site.register(Deck)
admin.site.register(Page)
admin.site.register(Character)
admin.site.register(RelDeck)
admin.site.register(Guide)
admin.site.register(Effects)
admin.site.register(RelGuide)
admin.site.register(AbnoCards)

from import_export import resources
from import_export.admin import ImportExportModelAdmin


# This is a small modification to make setting large amount of card's offices differently easier

class CardResource(resources.ModelResource):
    class Meta:
        model = Card


class CardAdmin(ImportExportModelAdmin):
    resource_class = CardResource
    _update_fields = (
        ("Make Rat", "make_rat", 1),
        ("Make Yun", "make_Yun", 2),
        ("Make Brotherhood of Iron", "make_Iron", 3),
        ("Make Hook", "make_Hook", 4),
        ("Make Pierre", "make_Pierre", 5),
        ("Make Streetlight", "make_Streetlight", 6),
        ("Make Zwei Association", "make_Zwei", 7),
        ("Make Stray Dogs", "make_Stray", 8),
        ("Make Molar", "make_Molar", 9),
        ("Make The Carnival", "make_Carnival", 10),
        ("Make Full Stop Office", "make_Full_Stop", 11),
        ("Make Dawn Office", "make_Dawn", 12),
        ("Make Gaze Office", "make_Gaze", 13),
        ("Make Kurokumo Clan", "make_Kurokumo", 14),
        ("Make Musicians of Bremen", "make_Musicians", 15),
        ("Make Wedge Office", "make_Wedge", 16),
        ("Make Love Town", "make_Love", 17),
        ("Make Sweepers", "make_Sweepers", 18),
        ("Make Shi Association", "make_Shi", 19),
        ("Make The 8' o clock circus", "make_circus", 20),
        ("Make Puppets", "make_Puppets", 21),
        ("Make Index Proselytes", "make_Index_Proselytes", 22),
        ("Make Smiling Faces", "make_Smiling", 23),
        ("Make Crying Children", "make_Crying", 24),
        ("Make Warp Cleanup Crew", "make_Warp", 25),
        ("Make Liu Association", "make_Liu", 26),
        ("Make Library", "make_Library", 27),
        ("Make Purple Tear", "make_purple", 44),
    )

    def get_actions(self, request):
        def func_maker(value):
            def update_func(self, request, queryset):
                queryset.update(Office=value)

            return update_func

        actions = super().get_actions(request)
        for description, function_name, value in self._update_fields:
            func = func_maker(value)
            name = "update_{}".format(function_name)
            actions["update_{}".format(function_name)] = (
                func,
                name,
                "Update {}".format(description),
            )

        return actions


admin.site.register(Card, CardAdmin)
