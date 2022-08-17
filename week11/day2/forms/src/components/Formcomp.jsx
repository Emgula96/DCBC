import React from 'react'

function Formcomp(props) {
  return (
    <div>Formcomp</div>
  )
}

export default Formcomp  


const checkData = () => {
    if (formData.firstName === '') { 
      window.alert('empy')
    }
  }

  const validateInput = (
    text,
    name,
  ) => {
    switch (name) {
      case "email":
        let emailValid = /\S+@\S+\.\S+/;
        setFormData({
          ...formData,
          [name]: text,
        });
        break;
      case "firstName":
        let namevalid = /^.{5,}$/;

        setFormData({
          ...formData,
          [name]: text,
        });
        break;
      case "lastName":
      let lnamevalid = /^.{5,}$/;
        setFormData({
          ...formData,
          [name]: text,
        });
        break;
      case "password":
      let passValid = /^.{5,}$/;
        setFormData({
          ...formData,
          [name]: text,
        });
        break;

      default:
        break;
    }
  };

  return (
    <div className="Formcomp">
      <div className="form-container">
        <h1>Form</h1>
        <p>Or sign up with</p>
        <form onSubmit={() => checkData()}>
          <div className="names-input">
          <input
            className="input-field"
            name="firstName"
            value={formData.name}
            onChange={(e) =>
              validateInput(
                e.target.value,
                e.target.name,
              )
            }
            placeholder="first name"
            type="text"
          />
          <input
            className="input-field"
            name="lastName"
            value={formData.name}
            onChange={(e) =>
              validateInput(
                e.target.value,
                e.target.name,
              )
            }
            placeholder="last name"
            type="text"
            />
            </div>
          <input
            className="input-field"
            name="email"
            value={formData.email}
            onChange={(e) =>
              validateInput(
                e.target.value,
                e.target.name,
              )
            }
            placeholder="email"
            type="text"
          />
          <input className="input-field"
            name="password"
            value={formData.password}
            onChange={(e) =>
              validateInput(
                e.target.value,
                e.target.name,
              )
            }
            placeholder="password"
            type="text"
          />
            <p>By creating an account you agree to the <a>terms and conditions </a></p>
          <input
            className="create-btn"
            type="submit"
            value="Create Account"
          />
        </form>
        <p>Template by Ethan and Jason</p>
      </div>
    </div>
  );
