import "./App.css";
import { useState } from "react";
import Formcomp from "./components/Formcomp";
import Output from "./components/Output";

function App() {
  const defaultForm = {
    firstName: "",
    password: "",
    lastName: "",
    email: "",
  };
  const [formData, setFormData] = useState(defaultForm);
  return (
    <div className="app">
      <Formcomp
        formData={formData}
        setFormData={setFormData}
        defaultForm={defaultForm}
      ></Formcomp>
      <Output
        formData={formData}
        setFormData={setFormData}
        defaultForm={defaultForm}
      ></Output>
    </div>
  );
}

export default App;
