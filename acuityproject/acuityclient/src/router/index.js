import {createRouter, createWebHashHistory} from 'vue-router'

import TasksRead from '../components/TasksRead.vue'
import LogIn from '../components/LogIn.vue'
import SignUp from '../components/SignUp.vue'
import AssessUser from '../components/AssessUser.vue'
import MyProfile from '../components/MyProfile.vue'
import OthersProfile from '../components/OthersProfile.vue'
import HomePage from '../components/HomePage.vue'

const About = { template: '<div>About</div>' }
const NotFound = { template: '<div>Not Found</div>'}

const routes = [
    { path: '/', component: TasksRead },
    { path: '/about', component: About },
    { path: '/users/:id', component: OthersProfile},
    { path: '/log-in', component: LogIn},
    { path: '/sign-up', component: SignUp},
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
    { path: '/assess/:id', component: AssessUser},
    { path: '/myprofile', component: MyProfile},
    { path: '/home-page', component: HomePage}
]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
})

router.routeApi = function(l){
    return 'https://acuity.srvz-webapp.he-arc.ch/api' + l
}

export default router