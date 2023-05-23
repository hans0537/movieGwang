<template>
  <div class="col-md-3 col-6">
    <h1>배우</h1>
    <div class="trend_2im clearfix position-relative">
      <div class="trend_2im1 clearfix">
        <div class="grid">
          <figure class="effect-jazz mb-0">
            <a href="#">
              <img :src="imgSrc" class="w-100 img-height" alt="img25">
              <div class="image-details" v-if="showDetails">
                <h6 class="col_red">{{ actor.name }}</h6>
              </div>
            </a>
          </figure>
        </div>
      </div>
      <div class="trend_2im2 clearfix text-center position-absolute w-100 top-0">
        <span class="fs-1">
          <a class="col_red" href="#"><i class="fa"></i></a>
        </span>
      </div>
    </div>

  </div>
</template>

<script>

export default {
  name:'ActorView',
  props: {
    actor: Object,
  },
  components: {

  },
  data() {
    return {
      imgSrc: "https://image.tmdb.org/t/p/w500" + this.movie.poster_path,
      overview: this.movie.overview.slice(0, 20) + "...",
      showDetails: false,
    }
  },
  computed: {
  },
  methods: {

  },
}
</script>

<style>

</style>