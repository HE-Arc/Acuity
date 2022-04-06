<template>
    <div class="row">
        <div class="column main-wrapper">
            <!-- First column Nothing here -->
        </div>

        <div class="column">
            <q-button @click="$router.push('/')" theme="link">Acuity</q-button>
        </div>

        <div class="column">
            <q-button @click="$router.push('/myprofile')" theme="secondary" type="icon" icon="" circle></q-button> <!-- TODO Include incon -->
        </div>
    </div>
</template>

<script>
export default {
    name: 'MainWrapper',
    data() {
        return{
        }
    },
    methods: {
        
    },
}
</script>
