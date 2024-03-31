<template>
    <div>
        <form action="">
            <input type="text" v-model="text">
            <button @click.stop.prevent="sendtopage">send</button>
        </form>
    </div>
</template>
<script>
export default {
    name: 'example_component',
    data(){
        return {
            text: ''
        }
    },
    methods: {
        sendtopage(){
            this.$emit('sendtopage', this.text)
            this.text = ''
        }
    }

}
</script>