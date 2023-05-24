<template>
  <div>
    <div class="container my-5">
      <div v-for="(movies, index) in AverageMovie" :key="index">
        <div class="row">
          <all-movie-items v-for="movie in movies" :key="movie.id" :movie="movie" class="col-2 mb-5"> </all-movie-items>
        </div>
      </div>
    </div>
    <!-- Pagination -->
    <div class="overflow-auto" style="display: flex; justify-content: center;">
      <!-- Use text in props -->
      <b-pagination
        v-model="currentPage"
        :total-rows="filteredMovies.length"
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
import AllMovieItems from '../components/MovieComponents/AllMovieItems.vue';

export default {
  name: 'ShowAllMovieView.vue',
  components: { AllMovieItems },
  data() {
    return {
      type: this.$route.params.type,
      rows: 100,
      perPage: 20,
      currentPage: 1,
      tmp: null,
      search_movie: null,
    };
  },

  computed: {
    AverageMovie() {
      const tmp1 = this.tmp.slice((this.currentPage - 1) * 20, this.currentPage * 20);
      let res = [];
      let temp = [];
      if (this.search_movie === null) {
        for (let i = 1; i <= tmp1.length; i++) {
          temp.push(tmp1[i - 1]);
          if (i % 4 === 0) {
            res.push(temp);
            temp = [];
          }
        }
        if (temp.length > 0) {
          res.push(temp);
        }
      } else {
        const searchKeyword = this.search_movie;
        for (let i = 1; i <= this.tmp.length; i++) {
          
          if (this.tmp[i - 1].title.includes(searchKeyword)) {
            temp.push(this.tmp[i - 1]);
          }
        }
        res.push(temp);
        temp = [];
      }
      return res;
    },
    pagedMovies() {
      const startIndex = (this.currentPage - 1) * this.perPage;
      return this.filteredMovies.slice(startIndex, startIndex + this.perPage);
    },

    filteredMovies() {
      if (this.search_movie === null) {
        return this.tmp;
      } else {
        const searchKeyword = this.search_movie.toLowerCase().trim();
        return this.tmp.filter(movie => movie.title.toLowerCase().includes(searchKeyword));
      }
    }
  },
  methods: {
    getPagelen() {
      let movies = null

      if (this.type == 'world') {
        movies = this.$store.state.user.worldcup_movies
      } else if (this.type == 'like') {
        movies = this.$store.state.user.like_movies
      }

      this.tmp = movies.sort((a, b) => -(a.popularity - b.popularity));
      this.rows = movies.length;
    },
    searchmovie() {
      // 가장 가까운 form의 input 요소 찾기
      const searchInput = this.$refs.searchInput;
      
      // 검색어 가져오기
      this.search_movie = searchInput.value.trim();
    },
    clearSearch() {
      const searchInput = this.$refs.searchInput;
      searchInput.value = ''; // 검색어 입력란 비우기
      this.search_movie = null; // 검색어 초기화
    }
  },
  created() {
    console.log(this.type)
    this.getPagelen();
  }
};
</script>

<style>
</style>
