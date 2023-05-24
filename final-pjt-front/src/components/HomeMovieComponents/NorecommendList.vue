<template>
  <section id="trend" class="pt-4 pb-5 mt-5">
    <div class="container">
      <div class="row trend_1" style="display:flex; justify-content: space-between;">
        <div class="hr-line"></div>
        <div class="col-md-6 col-6">
          <h4 class="trend_1l" style="text-align:left;">{{ user?.username || 'Anonymous' }}님 추천<span class="col_red"> 영화</span></h4>
        </div>
        <div class="col-md-6 col-6 text-end">
          <h6 class="mb-0" style="margin-right:10px;">
            {{ recommendationMessage }}
          </h6>
        </div>
      </div>
    </div>
    <div class="col-md-6 col-6 text-end">
      <router-link v-if="user !== null &&  user?.username !=='' " :to="{ name: 'worldcup' }" class="btn btn-success">영화 월드컵</router-link>
    </div>
  </section>
</template>

<script>
export default {
  name: 'NorecommendList',
  data() {
    return {
      user: null,
    }
  },
  computed: {
    recommendationMessage() {
      if (this.user.username ==='') {
        return '회원가입을 해주시면 유저님만을 위한 영화를 추천해드립니다.';
      } else {
        return `확보된 데이터가 없습니다. 영화 추천을 위해 영화 상세페이지에서 한개 이상의 영화에 대해 좋아요를 눌러주시기 바라며 Community 내 영화 월드컵을 1회 이상 진행 해주시기 바랍니다.`;
      }
    },
  },
  created() {
    this.user = this.$store.state.user;
    this.$store.dispatch('getuser')
  },
}
</script>

<style>
</style>