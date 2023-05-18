<template>
  <div class="home container">
    <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="@/assets/background.jpeg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="@/assets/logo.png" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="@/assets/background.jpeg" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <hr>

    <LatestList/>
    <hr>

    <UpComingList/>
  </div>

</template>

<script>
import LatestList from '@/components/HomeMovieComponents/LatestList'
import UpComingList from '@/components/HomeMovieComponents/UpComingList'

export default {
  name: 'HomeView',
  components: {
    LatestList,
    UpComingList,
  },
  created() {
    this.getLatest()
    this.getUpComing()
  },
  methods: {
    getLatest(){
      this.$store.dispatch('getLatest')
    },
    getUpComing(){
      this.$store.dispatch('getUpComing')
    },

  }
}
</script>

<style scoped>

</style>