<template>
<section id="trend" class="pt-4 pb-5">
  <div class="container">
    <div class="row trend_1">
      <div class="col-md-6 col-6">
      <div class="trend_1l">
        <h4 class="mb-0"><i class="fa fa-youtube-play align-middle col_red me-1"></i> Latest <span class="col_red">Movies</span></h4>
      </div>
      </div>
      <div class="col-md-6 col-6">
      <div class="trend_1r text-end">
        <h6 class="mb-0"><a class="button" href="#"> View All</a></h6>
      </div>
      </div>
    </div>

    <div class="row trend_2 mt-4">
      <div id="carouselExampleCaptions1" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="0" class="active" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="1" aria-label="Slide 2" class="" aria-current="true"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="2" aria-label="Slide 3" class="" aria-current="true"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="3" aria-label="Slide 4" class="" aria-current="true"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions1" data-bs-slide-to="4" aria-label="Slide 5" class="" aria-current="true"></button>
        </div>
        
        <div class="carousel-inner"> 
          <div class="carousel-item active" v-for="(movies, index) in latestList" :key="index">
            <div class="trend_2i row">
              <LatestListItem 
              v-for="movie in movies" :key="movie.id" :movie="movie"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- team dj begin -->
  <!-- <div class="team-dj">
      <div class="container">
          <div class="row justify-content-center">
              <div class="col-xl-8 col-lg-8">
                  <div class="add-space section-title text-center">
                      <h2>Top DJs</h2>
                  </div>
              </div>
          </div>
          <div class="row">
              <div class="col-xl-12 col-lg-12">
                  <div class="dj-slider">
                    <LatestListItem />
                  </div>
              </div>
          </div>
      </div>
  </div> -->
  <!-- team dj end -->

  <!-- <div class="container">
    <h1 class="text-center my-5">상영 중인 영화</h1>
    <div class="row">
      <div class="col">
        <div id="movie-slider" class="carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li v-for="(movie, index) in latestList" :key="movie.id" :data-target="'#movie-slider'" :data-slide-to="index" :class="{'active': index === 0}"></li>
          </ol>
          <div class="carousel-inner">
            <div v-for="(movie, index) in latestList" :key="movie.id" :class="{'carousel-item': true, 'active': index === 0}">
              <LatestListItem :movie="movie" />
            </div>
          </div>
          <a class="carousel-control-prev" href="#movie-slider" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">이전</span>
          </a>
          <a class="carousel-control-next" href="#movie-slider" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">다음</span>
          </a>
        </div>
      </div>
    </div>
  </div> -->
</template>

<script>
import LatestListItem from '@/components/HomeMovieComponents/LatestListItem'

export default {
  name: 'LatestList',
  components: {
    LatestListItem,
  },
  computed: {
    latestList() {
      const tmp = this.$store.state.latestList
      let res = []
      let temp = []
      for (let i = 1; i <= tmp.length; i++) {
        temp.push(tmp[i - 1])
        if(i % 4 == 0) {
          res.push(temp)
          temp = []
        }
      }
      return res
    }
  }
}
</script>

<style>
</style>
