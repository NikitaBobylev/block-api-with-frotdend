<template>
  <div>
        <div class="container">
      <div class="text-center">
        <form class="form-signin" @submit.prevent='sendlogin'>
          <h1 class="h3 mb-3 mt-3 font-weight-normal">
            Для входа укажите имя пользователя и пароль
          </h1>
          <label for="inputUsername" class="sr-only">Имя пользователя</label>
          <input
            id="inputUsername"
            class="form-control"
            placeholder="Имя пользователя"
            required=""
            v-model="login.username"
          />
          <label for="inputPassword" class="sr-only">Пароль</label>
          <input
            type="password"
            id="inputPassword"
            class="form-control mt-2"
            placeholder="Пароль"
            required=""
            v-model="login.password"
          />
          <label for="ReInputPassword" class="sr-only">Повторите пароль</label>
          <button 
          class="btn mt-2 btn-lg btn-primary btn-block" type="submit">
            Войти
          </button>
        </form>
      </div>
    </div>

  </div>
</template>
  
<script>
import axios from 'axios'
  export default {
    name: "singin",
    data(ctx){
      console.log(ctx.$auth)
      return {login :{
        username: '',
        password: '',
      }};
    },
    methods : {
      async sendlogin(){
        try {
            let response  = await this.$auth.loginWith('local', {data: this.login})
            .then(this.$router.push('/'));
        }catch(e){
          console.log(e);
        };
      }
    }
  }
  </script>
  
  <style scoped>
  
  </style>