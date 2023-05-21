import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
const API_KEY = 'a719d72e722ce5b82da9a04d59337764'
const TMDB_URL = 'https://api.themoviedb.org/3'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [],
    accessToken: null,
    latestList: null,
    upcomingList: null,
    popularMovie: null,
    allmovie: null,
  },
  getters: {
    isLogin(state) {
      return state.accessToken ? true : false
    }
  },
  mutations: {
    GET_LATEST(state, latest) {
      state.latestList = latest
    },

    GET_UPCOMING(state, upcoming) {
      state.upcomingList = upcoming
    },
    GET_POPULAR(state, popular) {
      state.popularMovie = popular
    },

    GET_ALL(state) {
      state.allmovie = [...new Set([...state.latestList, ...state.upcomingList, ...state.popularMovie])]
    },

    GET_ARTICLES(state, articles) {
      state.articles = articles
    },

    SAVE_SIGNUP_TOKEN(state, access) {
      state.accessToken = access
      router.push({name: 'login'})
    },
    SAVE_LOGIN_TOKEN(state, access) {
      state.accessToken = access
      alert("로그인 성공!!")
      router.go(-1)
    },
    LOGOUT(state) {
      state.accessToken = null
      alert('로그아웃 되셨습니다.')
      // 중복 routing 오류 방지
      const currentRoute = router.currentRoute;
      console.log(currentRoute)
      if (currentRoute.name != 'home') {
        router.push({ name: 'home' });
      }

    }
  },
  actions: {
    login(context, access) {
      context.commit('SAVE_LOGIN_TOKEN', access)
    },
    signup(context, access) {
      context.commit('SAVE_SIGNUP_TOKEN', access)
    },
    logout(context) {
      context.commit('LOGOUT')
    },

    // 상영중인 최신 영화
    getLatest(context) {
      const requests = []
      for (let page = 1; page <= 5; page++) {
        const request = axios({
          method: 'get',
          url: `${TMDB_URL}/movie/now_playing?language=ko-kr&page=${page}&region=kr&api_key=${API_KEY}`,
        })
        requests.push(request)
      }

      Promise.all(requests)
        .then((responses) => {
          const latest = []
          for (const response of responses) {
            latest.push(...response.data.results)
          }
          context.commit('GET_LATEST', latest)
        })
        .catch((err) => {
          console.log(err)
        })
    },

    // 개봉 예정작
    getUpComing(context) {
      axios({
        method: 'get',
        url: `${TMDB_URL}/movie/upcoming?language=ko-kr&region=kr&api_key=${API_KEY}`,
      })
        .then((res) => {
          // 제외 조건을 확인하여 유효한 개봉 예정작만 필터링
          const upcoming = res.data.results.filter(movie => movie.poster_path !== null && movie.overview.trim() !== '');
          context.commit('GET_UPCOMING', upcoming);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 인기영화
    popularMovie(context) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
      })
        .then(res => {
          context.commit('GET_POPULAR', res.data)
        })
    },

    // 게시글 가져오기
    getArticles(context) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/articles/',
        headers: {
          Authorization: `Bearer ${context.state.accessToken}`
        }
      })
        .then((res) => {
          console.log(res.data, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getall(context) {
      context.dispatch('getLatest').then(() => {
        context.dispatch('getUpComing').then(() => {
          context.dispatch('popularMovie').then(() => {
            context.commit('GET_ALL')
          })
        })
      })
    }
  },
  modules: {
  }
})
