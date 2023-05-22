import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import FindPwView from '../views/FindPwView.vue'
import FindUsernameView from '../views/FindUsernameView.vue'
import MovieView from '../views/MovieView.vue'
import CommunityView from '../views/CommunityView.vue'
import MyPageView from '../views/MyPageView.vue'
import ArticlesView from '@/components/CommunityComponents/ArticlesView'
import ChoQuizView from '@/components/CommunityComponents/ChoQuizView'
import OverQuizView from '@/components/CommunityComponents/OverQuizView'
import WorldcupView from '@/components/CommunityComponents/WorldcupView'
import ArticleCreateView from '@/components/CommunityComponents/ArticleCreateView'
import ArticleDetailView from '@/components/CommunityComponents/ArticleDetailView'

import AllMovieView from '@/components/MovieComponents/AllMovieView'
import AverageMovieView from '@/components/MovieComponents/AverageMovieView'
import GenreMovieView from '@/components/MovieComponents/GenreMovieView'
import NowMovieView from '@/components/MovieComponents/NowMovieView'
import UpcomingView from '@/components/MovieComponents/UpcomingView'
import ActionMovieView from '@/components/MovieComponents/ActionMovieView'
import AdventureMovieView from '@/components/MovieComponents/AdventureMovie'

import ArticleUpdateView from '@/components/CommunityComponents/ArticleUpdateView'

import UserProfileView from '../views/UserProfileView.vue'
import FriendsListView from '../views/FriendsListView.vue'

import store from '../store/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView,
    children: [
      {
        path:'/movie/all',
        name:'allmovie',
        component:AllMovieView
      },
      {
        path:'/movie/genre',
        name:'genremovie',
        component:GenreMovieView,
        children : [
          {
            path:'/movie/genre/action',
            name:'actionmovie',
            component:ActionMovieView,
          },
          {
            path:'/movie/genre/adventure',
            name:'adventuremovie',
            component:AdventureMovieView,
          },
        ]
      },
      {
        path:'/movie/average',
        name:'averagemovie',
        component:AverageMovieView
      },
      {
        path:'/movie/now',
        name:'nowmovie',
        component:NowMovieView
      },
      {
        path:'/movie/upcoming',
        name:'upcomingmovie',
        component:UpcomingView
      },
    ]
  },  
  {
    path: '/findPw',
    name: 'findPw',
    component: FindPwView
  },  
  {
    path: '/findUsername',
    name: 'findUsername',
    component: FindUsernameView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView,
    children: [
      {
        path: '/community/articles',
        name: 'articles',
        component: ArticlesView
      },
      {
        path: '/community/articles/create',
        name: 'articlesCreate',
        component: ArticleCreateView
      },
      {
        path: '/community/articles/update/:id',
        name: 'articleUpdate',
        component: ArticleUpdateView,
      },
      {
        path: '/community/articles/:id',
        name: 'articleDetail',
        component: ArticleDetailView,
      },
      {
        path: '/community/choquiz',
        name: 'choquiz',
        component: ChoQuizView
      },
      {
        path: '/community/overquiz',
        name: 'overquiz',
        component: OverQuizView
      },
      {
        path: '/community/worldcup',
        name: 'worldcup',
        component: WorldcupView
      },
    ]
  },

  {
    path: '/mypage',
    name: 'mypage',
    component: MyPageView
  },
  {
    path: '/userprofile/:id',
    name: 'userprofile',
    component: UserProfileView
  },
  {
    path: '/friendslist/:id',
    name: 'friendslist',
    component: FriendsListView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 로그인 여부
  const isLoggedIn = store.getters.isLogin

  // 로그인이 필요한 페이지 지정
  const authPages = ['articlesCreate', 'articleDetail', 'choquiz', 'overquiz', 'worldcup', 'mypage', 'friendslist']
  
  // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('해당 서비스는 로그인후에 이용 가능합니다')
    next({ name: 'login'})
  } else {
    next()
  }
})

export default router
