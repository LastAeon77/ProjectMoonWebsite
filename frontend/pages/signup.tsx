import { useRouter } from "next/router";
import { Formik, Form, Field, ErrorMessage } from "formik";
import { Box } from "@mui/system";
import { Button } from "@mui/material";
import axios from "axios";
type errors = {
  email?: string;
  username?: string;
  password?: string;
};

const Signup = () => {
  const router = useRouter();
  const prevUrl = router.query.prevUrl;
  // const [JWT, setJWT] = useState<string | null>("");
  return (
    <div className="bg-lor bg-fixed overflow-auto bg-contain h-screen">
      {/* <Navbar /> */}
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
              initialValues={{ email: "", username: "", password: "" }}
              validate={(values) => {
                const errors: errors = {};
                if (!values.email) {
                  errors.email = "Required";
                } else if (
                  !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)
                ) {
                  errors.email = "Invalid email address";
                }
                if (!values.username) {
                  errors.username = "Required";
                }
                if (!values.password) {
                  errors.password = "Required";
                }
                else if(values.password.length < 8){
                  errors.password = "It needs to be at least 8 characters"
                }
                return errors;
              }}
              onSubmit={(values, { setSubmitting }) => {
                localStorage.clear();
                axios
                  .post("api/user/create/", {
                    username: values.username,
                    email: values.email,
                    password: values.password,
                  })
                  .then((res) => {
                    localStorage.setItem("access_token", res.data.access);
                    localStorage.setItem("refresh_token", res.data.refresh);
                    router.push(`/${prevUrl}`);
                  })
                  .catch((errors) => {
                    console.log(errors.response.data);
                    alert(JSON.stringify(errors.response.data));
                  });

                setTimeout(() => {
                  // alert(JSON.stringify(values, null, 2));
                  setSubmitting(false);
                }, 400);
              }}
            >
              {({ isSubmitting }) => (
                <Form>
                  <div className="flex flex-col justify-center m-8">
                    <div>
                      <div className="flex flex-row text-white mb-5">
                        <p className="mr-3">
                          Email&nbsp;
                          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:{" "}
                        </p>
                        <Field
                          style={{ color: "black" }}
                          type="email"
                          name="email"
                        />
                        <ErrorMessage name="email">
                          {(msg) => <div style={{ color: "red" }}>{msg}</div>}
                        </ErrorMessage>
                      </div>
                    </div>
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

export default Signup;
