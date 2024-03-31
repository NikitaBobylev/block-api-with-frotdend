<template>
    <div>
      <StaticSlider :title='post.title'/>


       <div class="container">
      <div class="row">
        <div class="col-lg-8 my-4">
          <!--    ЭТО ТЕЛО ПОСТА -->

          <img class="img-fluid rounded" :src="post.image" alt="" />
          <hr />
          <div v-html="post.content" class="lead"></div>
          <hr />
          <p class="lead text-right">Автор: <a href="#">{{ post.author }}</a></p>
          <hr />
          <div class="text-right">Опубликовано {{ post.created_at }}</div>

          ЭТО КОМПОНЕНТ С КОММЕНТАРИЯМИ
          <form v-if="userisauth" action="" method="post" @submit.prevent='sendcomment'>
            <div class="card my-4">
            <div class="card-header">Прокомментируй</div>
            <div class="card-body">
              <div class="form-group">
                <textarea
                  class="form-control"
                  id="exampleFormControlTextarea1"
                  rows="3"
                  v-model="currentcomment"
                ></textarea>

              </div>

              <button
                type="submit"
                class="btn btn-primary">Отправить
              </button> 
            </div>
            </div>

          </form>


          <div v-for="comment in comments" :key="comment" class="media mb-4 mt-5">
            <img
              src="http://placehold.it/50x50"
              class="d-flex mr-3 rounded-circle"
              alt=""
            />
            <div  class="media-body">
              <h5 class="mt-0">{{ comment.author }}</h5>
               <p>{{ comment.text }}</p>
            </div>
          </div>

        </div>

        <div class="col-lg-4">
          <div class="card my-4">
            <div class="card-header">Теги</div>
            <div class="card-body">
              <div class="row">
                <div class="col-lg-6">
                  <ul class="list-unstyled mb-0">
                    <li v-for="tag in post.tags" :key="tag">
                      <nuxt-link :to="`/tags/${tag}`">{{ tag }}</nuxt-link>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <div class="card my-4">
            <h5 class="card-header">Последние статьи</h5>
            <div v-for="last_post in lastFivePosts" :key="last_post" class="card-body">
              <h5 class="card-title">{{ last_post.title }}</h5>
              <p class="card-text description truncate" v-html="last_post.content"></p>
              <nuxt-link :to="`/posts/${last_post.slug}`"
               class="card-link">Читать</nuxt-link>
               <hr/>
            </div>


          </div>
        </div>
      </div>
    </div> 
</div>
</template>
<script>

    // import StaticSlider from '~/components/static_slider';
    import axios from 'axios';
    export default {
        async asyncData({ params }){
          let postSlug = params.slug;
          const post = await axios.get(
            `http://127.0.0.1:8000/api/posts/${postSlug}/`).then(res => res.data);
          const comments = await axios.get(
            `http://127.0.0.1:8000/api/comments/${postSlug}/`).then(res => res.data);
          const lastFivePosts = await axios.get(
            `http://127.0.0.1:8000/api/aside/${postSlug}`).then(res => res.data);
          return {
            post: post,
            comments: comments,
            lastFivePosts: lastFivePosts,
            currentcomment: ''
          }

        },
        methods: {
          async sendcomment(){
            const response = await axios.post('http://localhost:8000/api/comments/', {
              'author': this.$auth.user.username,
              'text': this.currentcomment,
              'post': this.$route.params.slug
            })
            this.currentcomment = ''
            this.comments.splice(0, 0, response.data)
          }
        },
        watchQuery: true,
        name: 'SlugPosts',
        computed: {
          userisauth(){
            return this.$auth.loggedIn;
          }
        },

    }
</script>



<style scoped>

</style>