$(function() {
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='LoginDocente']").validate({
      //Reglas de validacion
      rules: {

        email: {
            required: true,
            email: true
        },

        password: {
            required: true
        },
       
      },
      // Mensajes especificos de error de validacion
      messages: {

        email: {
          required:"Por favor, introduzca una dirección de correo",
        },

        password: {
            required: "Por favor, introduzca la contraseña",
        },
      },
      submitHandler: function(form) {
        form.submit();
      }
    });
  });