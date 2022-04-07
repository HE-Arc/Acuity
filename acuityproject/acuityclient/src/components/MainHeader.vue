<template>
    <div class="header" :class="{fixed : isFixed}">
        <q-row v-if="!isClose" class="block__row w100 h100 margin0" align-v="center">
            <q-col class="block__col h100 logo-container" cols="2"><img class="logo block__content" src="../assets/Vector.svg"></q-col>
            <q-col class="block__col" cols="8"><h1>Acuity</h1></q-col>
            <q-col class="block__col" cols="2" offset="-1">
                <q-button class="float-right" @click="buttonClick()" theme="secondary" type="icon" icon="q-icon-account" circle></q-button>
            </q-col>
        </q-row>
        <q-button class="close-button" v-if="isClose" @click="$router.push('/')" theme="secondary" type="icon" icon="q-icon-close" circle></q-button>
    </div>
</template>

<script>
export default {
    name: 'MainHeader',
    props:['isFixed', 'isClose'],
    data() {
        return{
        }
    },
    methods: {
        buttonClick(){
            const connected = localStorage.getItem("token")
            if (connected === null)
                this.$router.push("/log-in")
            else
                this.$router.push("/myprofile")
        }
    },
}
</script>
