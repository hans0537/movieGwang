<template>
  <div class="container">
    <h1>초성 퀴즈</h1>
    <div class="row justify-content-center">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title text-center">초성 퀴즈</h3>
            <div class="text-center mb-4">
              <img src="../../assets/blackboard.png" alt="chalkboard" class="img-fluid">
            </div>
            <div class="text-center">
              <h4 class="card-subtitle mb-4">초성:asdf</h4>
              <!-- <div v-if="showResult">
                <h5 class="text-success" v-if="isCorrect">정답입니다!</h5>
                <h5 class="text-danger" v-else>오답입니다!</h5>
              </div>
              <input type="text" v-model="answer" class="form-control" :disabled="showResult">
              <button class="btn btn-primary mt-3" @click="checkAnswer" :disabled="showResult">확인</button> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChoQuizView',
  // methods: {
  //   get
  // },
  created() {
    console.log(this.$store.state.allmovie)
  }
}
</script>

<style>

</style>