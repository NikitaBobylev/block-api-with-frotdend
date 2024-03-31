<template> <div> <div class="container"> <div class="text-center"> <form class="form-signin"> <h1 class="h3 mb-3 mt-3 font-weight-normal">
            Для регистрации укажите имя пользователя и пароль
          </h1>
          <label for="inputUsername" class="sr-only">Имя пользователя</label>
          <input
            id="inputUsername"
            class="form-control"
            placeholder="Имя пользователя"
            required=""
            v-model="form.username"
          />
          <label for="inputPassword" class="sr-only">Пароль</label>
          <input
            type="password"
            id="inputPassword"
            class="form-control mt-2"
            placeholder="Пароль"
            v-model="form.password"
            required=""
          />
          <label for="ReInputPassword" class="sr-only">Повторите пароль</label>
          <input
            type="password"
            id="ReInputPassword"
            class="form-control mt-2"
            placeholder="Повторите пароль"
            v-model="form.password2"
            required=""
          />
          <button class="btn mt-2 btn-lg btn-primary btn-block"
          @click.stop.prevent='registr()' :disabled='!isComplete' type="submit">
            Регистрация
          </button>
        </form>
      </div>
    </div>

    </div>
</template>

<script>
import axios from 'axios'
  export default {
    name: "registraiton",
    data(ctx){
      return {
        form: {
          username: '',
          password: '',
          password2: ''
        }
      };
    },
    methods: {
       registr(){
        let registerFormData = new FormData()
        registerFormData.set('username', this.form.username)
        registerFormData.set('password', this.form.password)
        registerFormData.set('password2', this.form.password2)
        try{
          axios({
          url: 'http://localhost:8000/api/registration/',
          method: 'post',
          data: registerFormData
        }).catch(
          function (response){
            console.log(response)
          }
        )
        }catch(e){
          console.log(e)
        }
        this.$router.push('/')
      }
   },
    computed: {
      isComplete(){
        return this.form.username && this.form.password && this.form.password2
      }
      
    }
  }
  </script>
  
  <style scoped>
  
  </style>