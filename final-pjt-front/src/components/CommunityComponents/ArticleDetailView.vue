<template>
  <section style="background-color: #eee;">
    <div class="container mt-1 pt-1">
      <div class="row d-flex justify-content-center">
        <div class="col-md-12 col-lg-12 col-xl-12">
          <div class="card">
            <div class="card-body">
              <h3 class="fw-bold mb-4">{{article?.title}}</h3>
              <div class="d-flex flex-start align-items-center">

                <img v-if="article?.user.image_base64" class="rounded-circle shadow-1-strong me-3"
                  :src="getImageSrc(article?.user.image_base64)" alt="avatar" width="40"
                  height="40" />
                
                <img v-else class="rounded-circle shadow-1-strong me-3"
                  src="../../assets/baseProfile.png" alt="avatar" width="40"
                  height="40" />

                

                  <div style="width:100%">
                    <div class="text-start">
                      <h6 class="fw-bold text-primary me-3" style="display: inline;">{{article?.user.username}}</h6>
                      <p class="text-muted small" style="display: inline;">{{formatDate(article?.created_at)}}</p>
                    </div>
                    <div class="text-end">
                      <p class="text-muted small mb-0" style="margin-left: auto;">조회수: {{article?.hit}}</p>
                    </div>
                  </div>
              </div>

              <div class="mt-3 mb-4 pb-2 text-start ps-3" style="margin-left: 70px; width: 80%">
                <img style="width: 100%;" class="my-3" v-if="article?.image_base64" :src="getImageSrc(article?.image_base64)" alt="Article Image">
                <hr v-if="article?.image_base64">
                <p class="mt-1">{{article?.content}}</p>
              </div>
              <div class="mb-3" style="display: flex; justify-content: end;">
                <button class="btn btn-success" @click="goBack">이전 페이지</button>
              </div>
              <div class="small d-flex justify-content-start fw-bold">
                <div class="d-flex align-items-center me-3" @click="like" style="cursor: pointer;">
                  <i class="far fa-thumbs-up me-2" :class="{ 'fa-solid' : likeCheck }" style="color: blue;"></i>
                  <p class="mb-0">Like</p>
                  <span class="ms-1 fs-6">{{article?.like_cnt}}</span>
                </div>
                <div class="d-flex align-items-center me-3" @click="commentToggle" style="cursor: pointer;">
                  <i class="far fa-comment-dots me-2" style="color: blue;"></i>
                  <p class="mb-0">Comment</p>
                  <span class="ms-1 fs-6">{{article?.comment_count}}</span>
                </div>
              </div>
            </div>

            <div v-if="commentShow" class="card-footer py-3 border-0" style="background-color: #f8f9fa;">
              <div class="d-flex flex-start w-100">

                <img v-if="checkUser.image_base64" class="rounded-circle shadow-1-strong me-3"
                  :src="getImageSrc(checkUser.image_base64)" alt="avatar" width="40"
                  height="40" />

                <img v-else class="rounded-circle shadow-1-strong me-3"
                  src="../../assets/baseProfile.png" alt="avatar" width="40"
                  height="40" />

                <div class="form-outline w-100">
                  <b-form-textarea
                    id="comment"
                    v-model="comment"
                    class="form-control" rows="4"
                    max-rows="6"
                    style="background: #fff;" :class="{'active' : comment}"
                    @keyup.enter="createComment"
                  ></b-form-textarea>
                  <label class="form-label" for="comment">Comment</label>
                </div>
              </div>
              <div class="float-end mt-2 pt-1">
                <button type="button" class="me-2 btn btn-primary btn-sm" @click="createComment">댓글 달기</button>
                <button type="button" class="btn btn-outline-primary btn-sm" @click="commentCancel">취소</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 댓글/ 대댓글 부분 -->
    <div class="container">
      <div class="row d-flex justify-content-center">
        <div class="col-md-12 col-lg-12 col-xl-12">
          <div class="card">
            <div class="card-body p-4">
              <h4 class="text-start mb-4 pb-2 fw-bold">댓글 목록</h4>
              <div class="row">
                <div class="col">
                  <ArticleCommentView 
                  v-for="comment in commentsList" :key="comment.id" 
                  :comment="comment" :articleId="id" 
                  :checkUser="checkUser"
                  @get-comments="getComments"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import ArticleCommentView from '@/components/CommunityComponents/ArticleCommentView'

export default {
  name: 'ArticleDetailView',
  components: {
    ArticleCommentView
  },
  data() {
    return {
      API_URL: this.$store.state.API_URL,

      id: parseInt(this.$route.params.id),
      commentShow: false,
      article: null,
      comment: '',
      commentsList: '',

      checkUser: this.$store.state.user,

      likeCheck: false,
    }
  },
  methods: {
    goBack() {
      window.history.back();
    },
    getArticle(){
      axios({
        method: 'get',
        url: `${this.API_URL}/articles/${this.id}/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then((res) => {
        this.article = res.data
        // 가져온 게시글 좋아요 목록에 회원이 있다면
        this.likeCheck = res.data.like_users.some(user => user.username === this.checkUser.username)
      })
      .catch((err) => console.log(err))
    },

    getComments() {
      axios({
        method: 'get',
        url: `${this.API_URL}/articles/${this.id}/comments/create_all/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then((res) => {
        this.commentsList = res.data
      })
      .catch((err) => console.log(err))
    },

    formatDate(dateString) {
      const date = new Date(dateString);
      const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' };
      return date.toLocaleDateString('en-US', options);
    },

    commentToggle() {
      this.commentShow = !this.commentShow
    },

    like() {
      axios({
        method: 'post',
        url: `${this.API_URL}/articles/${this.id}/like/`,
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then(() => {
        this.likeCheck = !this.likeCheck
        this.getArticle()
      })
      .catch((err) => {
        console.log(err)
        alert('로그인 후에 이용해주세요')
      })
    },

    createComment() {
      axios({
        method: 'post',
        url: `${this.API_URL}/articles/${this.id}/comments/create_all/`,
        data: {
          content: this.comment
        },
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
      .then(() => {
        this.comment = ''
        this.commentShow = false
        this.getComments()
        this.getArticle()
      })
      .catch((err) => console.log(err))
    },

    commentCancel() {
      this.comment = ''
      this.commentShow = false
    },

    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
    },

  },
  mounted() {
    this.getArticle()
    this.getComments()
  }
}
</script>

<style>

</style>