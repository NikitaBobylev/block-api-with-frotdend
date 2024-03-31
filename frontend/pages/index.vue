ndex.vue

<template>
  <!-- <h1>Привет, это главная страница</h1>
  <div v-for="post in posts" :key="post.slug" class="blog">
    <div class="blog-title">{{ post.h1 }}</div>
    <div class="blog-introtext">{{ post.description }}</div>
    <div class="blog-tag">{{ post.tags }}</div>
  </div>
</div> -->

<div>
  <div class="container">
      <h1 class="my-4">Последние записи блога</h1>
     <div class="row">

      <div v-for="post in posts" :key="post.slug" class="col-md-4">
          <div class="card mb-4 shadow-sm">
            <img :src="post.image" alt="" class="card-img-top" />
            <div class="card-body">
              <h4 class="card-title">{{ post.title }}</h4>
              <div class="card-text mb-0 truncate" v-html="post.content"></div>
              <span class="mb-2" v-for="tag in post.tags" :key="tag">
                <nuxt-link :to="`tags/${tag}`" class="mr-1 badge badge-info">#{{ tag }}</nuxt-link>
              </span>

              <div class="d-flex justify-content-between align-items-center">

                <div class="btn-group mt-2">
                  <nuxt-link :to="`/posts/${post.slug}`" class="btn btn-sm btn-outline-secondary"
                    >Подробнее</nuxt-link
                  >
                </div>
                <small class="text-muted">{{ post.created_at }}</small>
              </div>
            </div>
          </div>
        </div>

     </div>
</div>

  <nav aria-label="Paginate me" class="mb-3">
      <ul class="pagination justify-content-center">

        <li v-if="!prev_page_exist" class="page-item disabled">
          <div class="page-link">Предыдущая</div>
        </li>

        <li v-else class="page-item">
          <nuxt-link class="page-link" :to="`?page=${now_page-1}`">Предыдущая</nuxt-link> 
        </li>
        
        <span v-for="page in pages" :key="page">
          <li v-if="page == now_page" class="page-item active">
            <nuxt-link class="page-link active" :to="`?page=${page}`">{{ page }}</nuxt-link>
          </li>

          <li v-else class="page-item">
            <nuxt-link class="page-link active" :to="`?page=${page}`">{{ page }}</nuxt-link>
          </li>
        </span>




        <li v-if="next_page_exist" class="page-item">
          <nuxt-link :to="`?page=${now_page+1}`" class="page-link">Следующая</nuxt-link>
        </li>

        <li v-else class="page-item disabled">
          <div class="page-link">Следующая</div>
        </li>
      </ul>
    </nav>


</div>

  

</template>

<script>
import axios from "axios";
export default {
  
  async asyncData(ctx) {
    function generatepagesaround(now_page, all_pages){
      let pagination_pages = []
      
      for (let nowp = now_page-2; nowp <= now_page+2; nowp++){
        if (nowp >= 1 && nowp <= all_pages){
          pagination_pages.push(nowp);
        };
      };
      return pagination_pages
    }
    
    const query = (ctx.query.page)? {'page': ctx.query.page}:{}
    const { data } = await axios.get(
      `http://127.0.0.1:8000/api/posts/`,
      {params: query});
    const now_page = Number(ctx.query.page) || 1
    
    return {
      posts: data.results,
      now_page: now_page,
      prev_page_exist: Boolean(data.previous),
      next_page_exist: Boolean(data.next),
      pages: generatepagesaround(now_page, Math.ceil(data.count / 6))
    }
  },
  methods: {
    
  },
  watchQuery: true,
  }

</script>

<style>

</style>
