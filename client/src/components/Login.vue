<template>
  <div class="container">
    <form>
      <div class="form-outline mb-4">
        <input type="email" id="emailinput" class="form-control" placeholder="email..."/>
      </div>

      <div class="form-outline mb-4">
        <input type="password" id="passwordinput" class="form-control" placeholder="password..."/>
      </div>

      <button 
        type="button" 
        class="btn btn-primary btn-block mb4"
        @click="handleSubmit"
      >
        Sign In
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: String,
      password: String,
    }
  },

  methods: {
    handleSubmit() {
      const path = "http://localhost:5001/login";
      const email = document.getElementById("emailinput").value;
      const password = document.getElementById("passwordinput").value;
      // console.log(`Email: ${email} | Password: ${password}`);

      document.getElementById("emailinput").value = "";
      document.getElementById("passwordinput").value = "";

      const userData = {
        email: email,
        password: password
      };
      // console.log(userData);
      axios.post(path, userData)
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.error(err);
        })
    }
  }
}
</script>