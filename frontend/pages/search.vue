<template>
    <div>
        <div class="container-fluid home-slider">
      <div
        id="carouselExampleCaptions"
        class="carousel slide"
        data-ride="carousel"
      >
        <div class="carousel-inner">
          <div
            class="carousel-item active"
            style="background-color: #343a40 !important"
          >
            <div class="carousel-caption d-none d-md-block">
              <div class="container">
                <form action="" mathod="post">
                  <input v-model="q" class="form-control" type="text" placeholder="Поиск" />
                  <button
                  @click.stop.prevent="makesearch()"
                  class="btn btn-outline-success mt-3" type="submit">
                    Поиск
                  </button>
                </form>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-lg-12 mt-5">

          <p class="lead">Найдено записей: {{ count }}</p>
            <div v-for="post in data.results" :key="post">
                <nuxt-link :to="`posts/${post.slug}`">
                    <h3>{{ post.title }}</h3>
                </nuxt-link>
                <p class="truncate" v-html="post.content"></p>
                <hr />
            </div>
        </div>
      </div>
    </div>
    </div>
</template>
<script>
import axios from 'axios'
    export default{
      watchQuery: ['q'],
      async asyncData(ctx){
        const { data } = await axios.get(
          `http://localhost:8000/api/posts/?search=${ctx.route.query.q}`)
        return {
          data: data,
          q: (ctx.route.query.q != 'null')? ctx.route.query.q : '',
          count: data.count
        }

      },
      methods: {
        makesearch(){
          this.$router.push('/search?q=' + this.q)
        }
      }
      

    }
</script>