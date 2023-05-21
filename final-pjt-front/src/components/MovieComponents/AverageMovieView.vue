<template>
  <div>
    <h1>인기 영화</h1>
    <div class="container">
      <div v-for="(movies, index) in AverageMovie" :key="index">
        <div>
          <div class="row">
            <AverageItems v-for="movie in movies" :key="movie.id" :movie="movie" class="col-2 mb-5"/>
          </div>
        </div>
      </div>
    </div>
        <!-- Pagination -->
        <div class="overflow-auto" style="display: flex; justify-content: center;">
          <!-- Use text in props -->
          <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            first-text="First"
            prev-text="Prev"
            next-text="Next"
            last-text="Last"
          ></b-pagination>
        </div>
    <!-- Pagination -->  
  </div>
</template>

<script>
import AverageItems from './AverageItems.vue';

export default {
  name: 'AverageMovieView',
  data() {
    return {
      rows: 100,
      perPage: 20,
      currentPage: 1,
      tmp:null,
    }
  },
  components: {
    AverageItems
  },
  computed: {
    AverageMovie() {
      const tmp1 = this.tmp.slice((this.currentPage-1)* 20,this.currentPage*20);
      let res = [];
      let temp = [];
      for (let i = 1; i <= tmp1.length; i++) {
        temp.push(tmp1[i - 1]);
        if (i % 4 === 0) {
          res.push(temp);
          temp = [];
          }
        }
      return res;
      }
    },
  methods: {
    getPagelen() {
      this.tmp = this.$store.state.popularMovie.sort((a, b) => -(a.popularity - b.popularity))
      this.rows = this.$store.state.popularMovie.length
    }
  },
  created() {
    this.getPagelen()
  }
};
</script>

<style>

</style>
