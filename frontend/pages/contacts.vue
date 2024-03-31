<template>
  <div>
    <StaticSlider :title="title"/>
    <div class="container">
      <div class="row">
        <div class="col-lg-12">

          <p class="lead mt-4">
            Чтобы связаться со мной заполните форму обратной связи
          </p>

          <form action="" class="mb-4">
            <div class="row">
              <div class="col-md-6">
                <div class="md-form mb-0">
                  <label for="name" class="sr-only">Ваше имя</label>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Ваше имя"
                    v-model="form.name"
                  />
                </div>
              </div>

              <div class="col-md-6">
                <div class="md-form mb-0">
                  <label for="inputEmail4" class="sr-only">Email</label>
                  <input
                    type="email"
                    class="form-control"
                    id="inputEmail4"
                    placeholder="Ваша почта"
                    v-model="form.email"
                  />
                </div>
              </div>
            </div>

            <div class="row mt-3">
              <div class="col-lg-12">
                <div class="md-form mb-0">
                  <label for="subject" class="sr-only">Тема</label>
                  <input
                    type="text"
                    id="subject"
                    class="form-control"
                    placeholder="Тема"
                    v-model="form.subject"
                  />
                </div>
              </div>
            </div>

            <div class="row mt-3">
              <div class="col-lg-12">
                <div class="md-form mb-0">
                  <label class="sr-only" for="exampleFormControlTextarea1"
                    >Ваше сообщение</label
                  >
                  <textarea
                    class="form-control"
                    id="exampleFormControlTextarea1"
                    rows="2"
                    placeholder="Ваше сообщение"
                    v-model="form.message"
                  ></textarea>
                </div>
              </div>
            </div>
            <div class="text-center text-md-left mt-3">
              <button class="btn btn-primary" type="submit"
              @click.prevent="submitForm" :disabled="!isComplete">Отправить</button>
            </div>
          </form>
        </div>
      </div>
    </div>

  </div>
</template>


  
<script>
  import StaticSlider from '~/components/static_slider'
  import axios from 'axios'
  export default {
    name: "contacts",
    data(){
      return {
        title: 'Связь не со мной',
        form: {
          name: '',
          email: '',
          subject: '',
          message: '',
        }
      }

    },
    components:{
      StaticSlider
    },
    methods:{
      submitForm(){
        let contactFormData = new FormData()
        contactFormData.set('name', this.form.name);
        contactFormData.set('email', this.form.email);
        contactFormData.set('subject', this.form.subject);
        contactFormData.set('message', this.form.message);
        axios({
          method: 'post',
          url: 'http://localhost:8000/api/feedback/',
          data: contactFormData,
        }).catch(function (response){
          console.log(response)
        })
        this.$router.push('/success')
      }
    },
    computed: {
      isComplete(){
      return this.form.name && this.form.email && this.form.subject && this.form.message
    }
    }


  }
  </script>
  
  <style scoped>
  
  </style>