<template>
    <div>
      <Navbar/>
      <Nuxt />
      <ThheFooter/>
    </div>
  </template>

<script>
  import Navbar from "~/components/navbar";
  import ThheFooter from "~/components/thefooter";
  export default {
    components: {
      Navbar,
      ThheFooter,
    }
  };
</script>
  
<style>
  
</style>