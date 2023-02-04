import axios from "axios";
import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import { Button, TextField } from "@mui/material";
import { Box } from "@mui/system";
import * as Yup from "yup";
import { Field, Form, Formik, FieldArray, getIn, useFormik } from "formik";
import {
  rank_id,
  card_id,
  office_id,
  effect_id,
  page_id,
} from "../../components/types";

const GenerateOptionPage = (data: page_id) => {
  return (
    <option key={data?.id} value={data?.id} style={{ color: "black" }}>
      {data?.Name}
    </option>
  );
};
const GenerateOptionOffice = (data: office_id) => {
  return (
    <option value={data?.id} key={data?.id} style={{ color: "black" }}>
      {data?.Name}
    </option>
  );
};
const GenerateOptionRank = (data: rank_id) => {
  return (
    <option value={data?.id} key={data?.Name} style={{ color: "black" }}>
      {data?.Name}
    </option>
  );
};
const GenerateOptionEffect = (data: effect_id) => {
  return (
    <option value={data?.id} key={data?.id} style={{ color: "black" }}>
      {data?.Name}: {data?.Description}
    </option>
  );
};
const GenerateOptionCard = (data: card_id) => {
  return (
    <option value={data?.id} key={data?.id} style={{ color: "black" }}>
      {data?.Name}
    </option>
  );
};
const DeckSchema = Yup.object().shape({
  Name: Yup.string()
    .min(2, "Too Short!")
    .max(50, "Too Long!")
    .required("Required"),
  Description: Yup.string().required("Required"),
  Recc_Floor: Yup.number().required("Required"),
  Recc_Page: Yup.number().required("Required"),
  Recc_Rank: Yup.number().required("Required"),
  cards: Yup.array()
    .of(
      Yup.object().shape({
        card: Yup.number().required("Required"),
        count: Yup.number().required("Required").min(1).max(3),
      })
    )
    .required("Must have cards")
    .min(3, "Minimum of 3 different cards")
    .max(9, "Only 9 different cards total")
    .test({
      name: "cards",
      message: "Total Must be equal to 9",
      test: function (value) {
        if (!value) return false;
        if (
          value.reduce((acc, curr) => {
            if (curr.count) {
              return acc + curr.count;
            } else {
              return acc;
            }
          }, 0) === 9
        ) {
          return true;
        }
        return false;
      },
    }),
  effects: Yup.array().of(
    Yup.object().shape({
      eff: Yup.number().required("Required or delete this section"),
    })
  ),
});
const CardArrayErrors = (errors: any) =>
  typeof errors.cards === "string" ? (
    <div style={{ color: "red" }}>{errors.cards}</div>
  ) : null;

const ErrorMessage = ({ name }: { name: string }) => (
  <Field
    name={name}
    style={{ color: "red" }}
    render={({ form }: { form: any }) => {
      const error = getIn(form.errors, name);
      const touch = getIn(form.touched, name);
      let temp: Array<string> = [];
      if (error) {
        let temp = error.split(" ").slice(1);
        const new_error = temp.join(" ");
        return touch && error ? (
          <div style={{ color: "red" }}>{new_error}</div>
        ) : null;
      }
      return null;
    }}
  />
);
const Createdeck = () => {
  // Check if user has logged in
  const router = useRouter();
  const [allcards, setcards] = useState<Array<card_id> | null>(null);
  const [floor, setFloor] = useState<Array<office_id> | null>(null);
  const [pages, setpages] = useState<Array<page_id> | null>(null);
  const [alleffects, seteffects] = useState<Array<effect_id> | null>(null);
  const [rank, setrank] = useState<Array<rank_id> | null>();
  useEffect(() => {
    // console.log(localStorage.getItem("access_token"));
    axios
      .get("api/checkauth", {
        headers: {
          Authorization: `JWT ${localStorage.getItem("access_token")}`,
          "Content-Type": "application/json",
          accept: "application/json",
        },
      })
      .catch((errors) => {
        router.push(`/login?prevUrl=lor/createdeck`);
      });
  }, []);
  useEffect(() => {
    axios
      .get("api/lor/cardid")
      .then((res) => setcards(res.data as Array<card_id>))
      .catch((error) => console.log(error));
    axios
      .get("api/lor/pageid")
      .then((res) => setpages(res.data as Array<page_id>))
      .catch((error) => console.log(error));
    axios
      .get("api/lor/officeid")
      .then((res) => setFloor(res.data as Array<office_id>))
      .catch((error) => console.log(error));
    axios
      .get("api/lor/effects")
      .then((res) => seteffects(res.data as Array<effect_id>))
      .catch((error) => console.log(error));
    axios
      .get("api/lor/rank")
      .then((res) => setrank(res.data as Array<rank_id>))
      .catch((error) => console.log(error));
  }, []);
  return (
    <div className="bg-lor bg-fixed overflow-auto bg-contain h-auto text-2xl">
      <div className="flex flex-row items-center justify-center">
        <Box
          sx={{
            width: 1800,
            height: 2000,
            backgroundColor: "black",
            opacity: [0.9, 0.9, 0.9],
          }}
          style={{
            boxShadow: `1px -20px 60px -20px purple inset, 0px 0px 5px -1px purple inset`,
          }}
        >
          <div className="flex flex-row items-center justify-center">
            <Formik
              initialValues={{
                Name: "",
                Description: "",
                Recc_Floor: "",
                Recc_Page: "",
                Recc_Rank: "",
                cards: [],
                effects: [],
              }}
              validationSchema={DeckSchema}
              onSubmit={(values, { setSubmitting }) => {
                const temp = values.cards.map((object) =>
                  JSON.stringify(object)
                );
                const new_card = temp.join("|");
                axios
                  .post(
                    "/api/lor/deckcreate/",
                    {
                      name: values.Name,
                      description: values.Description,
                      cards: new_card,
                      show: true,
                      Recc_Floor: parseInt(values.Recc_Floor),
                      Recc_Page: parseInt(values.Recc_Page),
                      Recc_Rank: parseInt(values.Recc_Rank),
                      effect: values.effects.map((object, i) =>
                        parseInt(object["eff"])
                      ),
                    },
                    {
                      headers: {
                        Authorization: `JWT ${localStorage.getItem(
                          "access_token"
                        )}`,
                        "Content-Type": "application/json",
                        accept: "application/json",
                      },
                    }
                  )
                  .then((res) => setTimeout(() => {}, 400))
                  .then((res) => router.push("/lor/deck/"))
                  .catch((error) =>
                    alert("The deck name probably already exists")
                  );
                setTimeout(() => {
                  setSubmitting(false);
                }, 400);
              }}
            >
              {({ errors, touched, isSubmitting, values }) => (
                <Form style={{ width: 600 }}>
                  <div className="flex flex-col justify-center text-white">
                    <p> Deck Name : </p>
                    <Field name="Name" style={{ color: "black" }} />
                    {errors.Name && touched.Name ? (
                      <div style={{ color: "red" }}>{errors.Name}</div>
                    ) : null}

                    <p> Description : </p>
                    <Field
                      name="Description"
                      style={{
                        height: 200,
                        color: "black",
                      }}
                    />
                    {errors.Description && touched.Description ? (
                      <div style={{ color: "red" }}>{errors.Description}</div>
                    ) : null}

                    <p> Recommended Floor : </p>
                    <Field
                      as="select"
                      name="Recc_Floor"
                      autoComplete="off"
                      style={{ color: "black" }}
                    >
                      <option value="" style={{ color: "black" }}>
                        {" "}
                        Please Select a Floor{" "}
                      </option>
                      {floor?.map((object, i) => GenerateOptionOffice(object))}
                    </Field>
                    {errors.Recc_Floor && touched.Recc_Floor ? (
                      <div style={{ color: "red" }}>{errors.Recc_Floor}</div>
                    ) : null}

                    <p> Recommended Page : </p>
                    <Field
                      as="select"
                      name="Recc_Page"
                      autoComplete="off"
                      style={{ color: "black" }}
                    >
                      <option value="" style={{ color: "black" }}>
                        {" "}
                        Please Select a Page{" "}
                      </option>
                      {pages?.map((object, i) => GenerateOptionPage(object))}
                    </Field>
                    {errors.Recc_Page && touched.Recc_Page ? (
                      <div style={{ color: "red" }}>{errors.Recc_Page}</div>
                    ) : null}

                    <p> Recommended Rank : </p>
                    <Field
                      as="select"
                      name="Recc_Rank"
                      autoComplete="off"
                      style={{ color: "black" }}
                    >
                      <option value="" style={{ color: "black" }}>
                        {" "}
                        Please Select a Rank{" "}
                      </option>
                      {rank?.map((object, i) => GenerateOptionRank(object))}
                    </Field>
                    {errors.Recc_Rank && touched.Recc_Rank ? (
                      <div style={{ color: "red" }}>{errors.Recc_Rank}</div>
                    ) : null}
                    <FieldArray
                      name="cards"
                      render={(arrayHelpers) => (
                        <div>
                          {values.cards.length > 0 &&
                            values.cards.map((cards, index) => (
                              <div key={index}>
                                <p>Card Name </p>
                                <Field
                                  as="select"
                                  name={`cards[${index}].card`}
                                  style={{ color: "black" }}
                                >
                                  <option value="" style={{ color: "black" }}>
                                    {" "}
                                    Please Select a Card{" "}
                                  </option>
                                  {allcards?.map((object, i) =>
                                    GenerateOptionCard(object)
                                  )}
                                </Field>
                                <ErrorMessage name={`cards[${index}].card`} />
                                <p>Number of cards </p>
                                <Field
                                  style={{ color: "black" }}
                                  name={`cards[${index}].count`}
                                />
                                <ErrorMessage name={`cards[${index}].count`} />
                                <Button
                                  variant="contained"
                                  type="button"
                                  onClick={() => arrayHelpers.remove(index)}
                                >
                                  Delete
                                </Button>
                              </div>
                            ))}
                          <Button
                            variant="contained"
                            type="button"
                            onClick={() =>
                              arrayHelpers.push({ card: null, count: 1 })
                            }
                          >
                            Add a Card
                          </Button>
                        </div>
                      )}
                    />
                    {CardArrayErrors(errors)}
                    <FieldArray
                      name="effects"
                      render={(arrayHelpers) => (
                        <div>
                          {values.effects.length > 0 &&
                            values.effects.map((cards, index) => (
                              <div key={index}>
                                <p>Effect: </p>
                                <Field
                                  as="select"
                                  name={`effects[${index}].eff`}
                                  style={{ color: "black", width: 400 }}
                                >
                                  <option value="" style={{ color: "black" }}>
                                    {" "}
                                    Please Select an Effect{" "}
                                  </option>
                                  {alleffects?.map((object, i) =>
                                    GenerateOptionEffect(object)
                                  )}
                                </Field>
                                <ErrorMessage name={`effects[${index}].eff`} />
                                <Button
                                  variant="contained"
                                  type="button"
                                  onClick={() => arrayHelpers.remove(index)}
                                >
                                  Delete
                                </Button>
                              </div>
                            ))}
                          <Button
                            variant="contained"
                            type="button"
                            onClick={() => arrayHelpers.push({ eff: null })}
                          >
                            Add an Effect
                          </Button>
                        </div>
                      )}
                    />
                    <Button
                      variant="contained"
                      type="submit"
                      disabled={isSubmitting}
                    >
                      Submit
                    </Button>
                  </div>
                </Form>
              )}
            </Formik>
          </div>
        </Box>
      </div>
    </div>
  );
};

export default Createdeck;
