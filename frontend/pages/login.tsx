import { useRouter } from "next/router";
import { useEffect } from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import { Box } from "@mui/system";
import { Button } from "@mui/material";
import axios from "axios";
type errors = {
  username?: string;
  password?: string;
};
const Login = () => {
  const router = useRouter();
  const prevUrl = router.query.prevUrl;
  useEffect(() => {
    if (localStorage) {
      const refresh = localStorage.getItem("refresh_token");
      axios
        .post("/api/token/refresh/", {
          headers: {
            "Content-Type": "application/json",
            accept: "application/json",
          },
          "refresh": refresh
        })
        .then((res) => {
          localStorage.setItem("access_token", res.data.access);
          localStorage.setItem("refresh_token", res.data.refresh);
          if (prevUrl!== null && prevUrl !== undefined) {
            router.push(`/${prevUrl}`);
          } else {
            router.push("/");
          }
        }).catch((error)=>console.log("Gotta login!"));
    }
  }, []);
  return (
    <div className="bg-lor bg-fixed overflow-auto bg-contain h-screen">
      <div className="flex flex-row items-center justify-center">
        <Box
          sx={{
            width: 1800,
            height: 900,
            backgroundColor: "black",
            opacity: [0.9, 0.9, 0.9],
          }}
          style={{
            boxShadow: `1px -20px 60px -20px purple inset, 0px 0px 5px -1px purple inset`,
          }}
        >
          <div className="flex flex-row items-center justify-center">
            <Formik
              initialValues={{ username: "", password: "" }}
              validate={(values) => {
                const errors: errors = {};
                if (!values.username) {
                  errors.username = "Required";
                } else if (!values.password) {
                  errors.password = "Required";
                }
                return errors;
              }}
              onSubmit={(values, { setSubmitting }) => {
                // axios.post("/api/users");
                axios
                  .post("api/token/obtain/", {
                    username: values.username,
                    password: values.password,
                  })
                  .then((res) => {
                    localStorage.setItem("access_token", res.data.access);
                    localStorage.setItem("refresh_token", res.data.refresh);
                    if (prevUrl) {
                      router.push(`/${prevUrl}`);
                    } else {
                      router.push("/");
                    }
                  });
                setTimeout(() => {
                  setSubmitting(false);
                }, 400);
              }}
            >
              {({ isSubmitting }) => (
                <Form>
                  <div className="flex flex-col justify-center m-8">
                    <div>
                      <div className="flex flex-row text-white">
                        <p className="mr-4">Username&nbsp;: </p>
                        <Field
                          style={{ color: "black" }}
                          type="username"
                          name="username"
                        />
                        <ErrorMessage name="username">
                          {(msg) => <div style={{ color: "red" }}>{msg}</div>}
                        </ErrorMessage>
                      </div>
                    </div>
                    <div>
                      <div className="flex flex-row text-white mt-5">
                        <p className="mr-4">Password &nbsp;: </p>
                        <Field
                          style={{ color: "black" }}
                          type="password"
                          name="password"
                        />
                        <ErrorMessage name="password">
                          {(msg) => <div style={{ color: "red" }}>{msg}</div>}
                        </ErrorMessage>
                      </div>
                    </div>
                  </div>
                  <Button
                    variant="contained"
                    type="submit"
                    disabled={isSubmitting}
                  >
                    Submit
                  </Button>
                </Form>
              )}
            </Formik>
          </div>
        </Box>
      </div>
    </div>
  );
};

export default Login;
