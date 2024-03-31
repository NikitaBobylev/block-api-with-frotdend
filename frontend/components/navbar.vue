<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarTogglerDemo01"
        aria-controls="navbarTogglerDemo01"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <nuxt-link class="navbar-brand" to="/">
          <img
            src="https://seeklogo.com/images/N/nuxt-logo-5EF50E1ABD-seeklogo.com.png"
            width="30"
            height="30"
            alt="logo"
          />
        </nuxt-link>
        <nuxt-link to="/" class="navbar-brand">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
            width="30"
            height="30"
            alt="logo"
          />
        </nuxt-link>

        <ul nuxt-link-active class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item">
            <nuxt-link nuxt-link-active class="nav-link" to="/"
              >Главная <span class="sr-only">(current)</span></nuxt-link
            >
          </li>
          <li class="nav-item">
            <nuxt-link nuxt-link-active class="nav-link" to="/contacts">Контакты</nuxt-link>
          </li>
        </ul>
        <form v-if="$route.name != 'search'" class="form-inline my-2 my-lg-0">
          <input
            class="form-control mr-sm-2"
            type="search"
            placeholder="Search"
            aria-label="Search"
            v-model="q"
          />
          <button
            class="btn btn-outline-success my-2 my-sm-0 mr-2"
            type="submit"
            @click.stop.prevent="submit()"
          >
            Поиск
          </button>
        </form>
          <span class="navbar-text mr-2" v-if="logginIn">{{ user_username }}</span>
          <span v-else>
          <nuxt-link class="btn btn-outline-info my-2 my-sm-0 mr-2" to="/singin">
            Вход
          </nuxt-link>
          <nuxt-link class="btn btn-outline-info my-2 my-sm-0 mr-2" to="/registration">
            Регистрация
          </nuxt-link>
          </span>
          <nuxt-link v-if="logginIn" class="btn btn-outline-info my-2 my-sm-0" to="/singout">
            Выход
          </nuxt-link>
      </div>
    </nav>
</template>

<script>
    export default {
        name: 'Navbar',
        data(){
            return {q: null}
        },
        methods: {
            submit(){
                this.$router.push('/search?q=' + this.q)
                this.q = null
            }
        },
        computed: {
          user_username(){
            console.log(this.$auth)
            return this.$auth.user.username
          },
          logginIn(){
             return this.$auth.loggedIn
          }
        }
    }
</script>



<style scoped></style>