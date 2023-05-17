<template>
<section class="vh-100" style="background-color:  #eee;">
  <b-container role="group" class="py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card shadow-2-strong" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <h3 class="mb-5">Sign in</h3>

            <b-row class="form-outline mb-4">
              <label class="form-label" for="input-username">아이디</label>
              <b-form-input class="form-control form-control-lg" id="input-username" placeholder="ID" v-model="username" :state="nameState" aria-describedby="input-username-feedback" trim></b-form-input>

              <b-form-invalid-feedback id="input-username-feedback" class="text-right">
                알파벳/숫자 3글자 이상
              </b-form-invalid-feedback>
<!-- 
              <input type="email" id="typeEmailX-2" class="form-control form-control-lg" />
              <label class="form-label" for="typeEmailX-2">Email</label> -->
            </b-row>

            <div class="form-outline mb-4">
              <input type="password" id="typePasswordX-2" class="form-control form-control-lg" />
              <label class="form-label" for="typePasswordX-2">Password</label>
            </div>

            <!-- Checkbox -->
            <div class="form-check d-flex justify-content-start mb-4">
              <input class="form-check-input" type="checkbox" value="" id="form1Example3" />
              <label class="form-check-label" for="form1Example3"> Remember password </label>
            </div>

            <button class="btn btn-primary btn-lg btn-block" type="submit">Login</button>

            <hr class="my-4">

            <button class="btn btn-lg btn-block btn-primary" style="background-color: #dd4b39;"
              type="submit"><i class="fab fa-google me-2"></i> Sign in with google</button>
            <button class="btn btn-lg btn-block btn-primary mb-2" style="background-color: #3b5998;"
              type="submit"><i class="fab fa-facebook-f me-2"></i>Sign in with facebook</button>
          </div>
        </div>
      </div>
    </div>
  </b-container>
</section>
</template>

<script>
import axios from 'axios'

export default {
  name: "LoginView",
  data() {
    return {
      username: '',
      password: '',
    }
  },
  computed: {
    nameState(){
      return this.username.length >= 3 ? true: false
    },
    pwState(){
      return this.password.length >= 10 ? true: false
    }
  },
  methods: {
    login() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/auth/login/',
        data: {
          username: this.username,
          password: this.password
        }
      })
      .then((res) => {
        console.log(res)
        this.$store.dispatch('login', res.data.access)
      })
      .catch((err) => console.log(err))
    }
  }
}
</script>

<style>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 700px;
}

.login-form {
  width: 50%;
  height: 500px;
  margin: 0 auto;
  border-radius: 15px;
  background-color: rgb(33, 34, 36);
  box-shadow: 20px 20px 10px 0px lightgray;
}

</style>