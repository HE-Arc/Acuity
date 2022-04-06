<template>
    <div class="header" :class="{fixed : isFixed}">
        <q-row class="block__row" align-v="center">
            <q-col class="block__content"><h1>Acuity</h1></q-col>
            <q-col class="block__content">
                <q-button @click="buttonClick()" theme="secondary" type="icon" icon="q-icon-account" circle></q-button>
            </q-col>
        </q-row>
    </div>
</template>

<script>
export default {
    name: 'MainHeader',
    props:['isFixed'],
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
