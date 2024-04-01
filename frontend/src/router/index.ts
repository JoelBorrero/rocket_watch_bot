import { createRouter, createWebHistory } from "vue-router";

class Routes {
  static howTo = "/how_to";
  static play = "/";
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: Routes.howTo,
      name: "how_to",
      component: () => import("../views/HowTo.vue"),
    },
    {
      path: Routes.play,
      name: "play",
      component: () => import("../views/Play.vue"),
    },
  ],
});

export default router;
export { Routes };
