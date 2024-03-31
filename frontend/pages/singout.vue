<template>
  <div></div>
</template>
  
<script>
  export default {
    name: "singout",
    async created(){
      await this.$auth.logout().
      then(this.$router.push(
        this.$nuxt.context.from.name))
    }
  }
  </script>
  
  <style scoped>
  
  </style>