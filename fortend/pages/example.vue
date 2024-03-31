<template>

    <div>
        <example-component @sendtopage="datafromcomponent = $event"/>
        <h1>eta infa iz componenta <span>{{ datafromcomponent }}</span></h1>
    </div>
</template>
<script>
    import example_component from '~/components/example_component'
    export default {
        components: { example_component },
        name: 'example',
        data(){
            return {
                datafromcomponent: '',
            };
            
        },
    };
</script>


