<template>
  <section class="vh-100" style="background-color: #eee;">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-lg-12 col-xl-11">
          <div class="card text-black" style="border-radius: 25px;">
            <div class="card-body p-md-5">
              <div class="row justify-content-center">
                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                  <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Sign up</p>

                  <form class="mx-1 mx-md-4">

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-user fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input type="text" id="form3Example1c" class="form-control" />
                        <label class="form-label" for="form3Example1c">Your Name</label>
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-envelope fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input type="email" id="form3Example3c" class="form-control" />
                        <label class="form-label" for="form3Example3c">Your Email</label>
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input type="password" id="form3Example4c" class="form-control" />
                        <label class="form-label" for="form3Example4c">Password</label>
                      </div>
                    </div>

                    <div class="d-flex flex-row align-items-center mb-4">
                      <i class="fas fa-key fa-lg me-3 fa-fw"></i>
                      <div class="form-outline flex-fill mb-0">
                        <input type="password" id="form3Example4cd" class="form-control" />
                        <label class="form-label" for="form3Example4cd">Repeat your password</label>
                      </div>
                    </div>

                    <div class="form-check d-flex justify-content-center mb-5">
                      <input class="form-check-input me-2" type="checkbox" value="" id="form2Example3c" />
                      <label class="form-check-label" for="form2Example3">
                        I agree all statements in <a href="#!">Terms of service</a>
                      </label>
                    </div>

                    <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                      <button type="button" class="btn btn-primary btn-lg">Register</button>
                    </div>

                  </form>

                </div>
                <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">

                  <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp"
                    class="img-fluid" alt="Sample image">

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
<!-- Section: Design Block -->
  <!-- <b-container role="group" class="p-5 login-form">
    <h1>회원가입</h1>
    <b-row>
      <label for="input-username">아이디</label>
      <b-form-input id="input-username" placeholder="ID" v-model="username" :state="nameState" aria-describedby="input-username-feedback" trim></b-form-input>

      <b-form-invalid-feedback id="input-username-feedback" class="text-right">
        알파벳/숫자 3글자 이상
      </b-form-invalid-feedback>
    </b-row>
    
    <b-row>
      <label for="input-password">비밀번호</label>
      <b-form-input id="input-password" type="password" placeholder="PASSWORD" v-model="password1" :state="pwState" aria-describedby="input-pw-feedback" trim></b-form-input>

      <b-form-invalid-feedback id="input-pw-feedback" class="text-right">
        비밀번호 10자 이상
      </b-form-invalid-feedback>
    </b-row>

    <b-row>
      <label for="input-password">비밀번호 확인</label>
      <b-form-input id="input-password" type="password" placeholder="PASSWORD" v-model="password2" :state="pwCheckState" aria-describedby="input-pwCheck-feedback" trim></b-form-input>

      <b-form-invalid-feedback id="input-pwCheck-feedback" class="text-right">
        비밀번호가 같지 않습니다
      </b-form-invalid-feedback>
    </b-row>
    <br>
    <b-button variant="success" @click="signup">로그인</b-button>
  </b-container> -->
</template>

<script>
import axios from 'axios'

export default {
  name: "SignupView",
  data() {
    return {
      username: '',
      password1: '',
      password2: '',
    }
  },
  computed: {
    nameState(){
      return this.username.length >= 3 ? true: false
    },
    pwState(){
      return this.password1.length >= 10 ? true: false
    },
    pwCheckState() {
      return this.password2 && this.password1 === this.password2 ? true: false
    }
  },
  methods: {
    signup() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/auth/signup/',
        data: {
          username: this.username,
          password1: this.password1,
          password2: this.password2
        }
      })
      .then((res) => {
        console.log(res)
        this.$store.dispatch('signup', res.data.access)
      })
      .catch((err) => console.log(err))
    }
  }
}
</script>

<style>
  .cascading-right {
    margin-right: -50px;
  }

  @media (max-width: 991.98px) {
    .cascading-right {
      margin-right: 0;
    }
  }
</style>
