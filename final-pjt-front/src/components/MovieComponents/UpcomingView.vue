<template>
  <div>
    <h1>상영 예정작</h1>
    <div class="container">
      <div v-for="(movies, index) in AverageMovie" :key="index">
        <div>
          <div class="row">
            <UpcomingItems v-for="movie in movies" :key="movie.id" :movie="movie" class="col-2 mb-5"/>
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
import UpcomingItems from './UpcomingItems.vue';
export default {
  name:'NowMovieView',
  data() {
    return {
      rows: 20,
      perPage: 20,
      currentPage: 1,
      tmp:null,
    }
  },
  components: {
    UpcomingItems
  },
  computed: {
  AverageMovie() {
    const tmp1 = this.tmp.slice((this.currentPage - 1) * 20, this.currentPage * 20);
    let res = [];
    let temp = [];
    for (let i = 1; i <= tmp1.length; i++) {
      temp.push(tmp1[i - 1]);
      if (i % 4 === 0) {
        res.push(temp);
        temp = [];
      }
    }
    // 개봉예정일 기준으로 정렬
    res.forEach((movies) => {
      movies.sort((a, b) => a.release_date.localeCompare(b.release_date));
    });
    return res;
  }
},
  methods: {
    getPagelen() {
    this.tmp = this.$store.state.upcomingList.sort((a, b) => a.release_date.localeCompare(b.release_date));
    this.rows = this.tmp.length;
  }
  },
  created() {
    this.getPagelen()
  }
}
</script>

<style>

</style>