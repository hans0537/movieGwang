<template>
  <div class="modal">
    <div class="modal-content">
      <div class="image-container">
        <img :src="imgSrc" class="w-50 img-height" alt="img25">
      </div>
      <h2>{{ movie.title }}</h2>
      <p>{{ movie.overview }}</p>
      <p>평점: {{ movie.vote_average }}</p>
      <!-- 추가적인 영화 정보를 표시하는 요소들을 추가합니다 -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieModal',
  props: {
    movie: Object
  },
  data() {
    return {
      imgSrc: "https://image.tmdb.org/t/p/w500" + this.movie.poster_path,
    }
  },
  mounted() {
    // 모달 외부를 클릭하면 모달을 닫도록 이벤트 리스너를 추가합니다
    window.addEventListener('click', this.closeModalOutside);
  },
  beforeDestroy() {
    // 컴포넌트가 파괴되기 전에 이벤트 리스너를 제거합니다
    window.removeEventListener('click', this.closeModalOutside);
  },
  methods: {
    closeModalOutside(event) {
      // 모달 외부를 클릭한 경우 모달을 닫습니다
      if (event.target.classList.contains('modal')) {
        this.$emit('close');
      }
    }
  }
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  width: 1000px;
  height:1100px;
  text-align: center;
}
</style>
