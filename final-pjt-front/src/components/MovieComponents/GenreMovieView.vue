<template>
  <div>
    <nav class="navbar bg-dark" data-bs-theme="dark">
      <div class="container">
        <router-link to="/movie/genre/action" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/action' }">액션</router-link>
        <router-link to="/movie/genre/adventure" class="nav-link" :class="{ 'active': $route.path === '/movie/genre/adventure' }">모험</router-link>
      </div>
    </nav>
    <router-view/>

  </div>
</template>

<script>
export default {
  name:'GenreMovieView',
  data() {
    return {

    }
  },
  computed: {

  }
}
</script>

<style>

</style>