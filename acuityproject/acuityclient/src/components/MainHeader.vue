<template>
    <div class="header" :class="{fixed : isFixed}">
        <q-row v-if="!isClose" class="block__row w100 h100 margin0" align-v="center">
            <q-col class="block__col h100 logo-container" cols="2"><img class="logo block__content" src="../assets/logo.svg"></q-col>
            <q-col class="block__col" cols="8"><h1>Acuity</h1></q-col>
            <q-col class="block__col" cols="2" offset="-1">

                <q-context-menu
                v-if="connected"
                :menu-items="menuItems"
                @action="buttonClick"
                >
                    <q-button theme="secondary" type="icon" icon="q-icon-account" circle></q-button>
                </q-context-menu>

                <q-button v-else @click="this.$router.push('/log-in')" theme="secondary" type="icon" icon="q-icon-login" circle></q-button>
                
            </q-col>
        </q-row>
        <q-button class="close-button" v-if="isClose" @click="$router.push('/')" theme="secondary" type="icon" icon="q-icon-close" circle></q-button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MainHeader',
    props:['isFixed', 'isClose'],
    data() {
        return{
            connected: localStorage.getItem("token") != null,
            menuItems: [
                {
                    action: 'profile',
                    name: 'Profile',
                    icon: 'q-icon-account'
                },
                {
                    action: 'log-out',
                    name: 'Log out',
                    icon: 'q-icon-logout'
                }
            ]
        }
    },
    methods: {                
        disconnect() {
            axios.post(this.$router.routeApi('/users/disconnect/'))
                .then(() => {
                    this.$store.commit('removeToken')
                    localStorage.removeItem('token')
                    axios.defaults.headers.common['Authorization'] = ''
                    
                    this.$router.push('/log-in')
                })
                .catch(error => {
                    console.log(error)
                })
        },

        buttonClick(action){
            switch (action){
                case 'log-out':
                    this.disconnect()
                    break
                case 'profile':
                default:
                    if (localStorage.getItem("token") == null)
                        this.$router.push("/log-in")
                    else
                        this.$router.push("/myprofile")
                    break
            }
        },
    },
}
</script>
