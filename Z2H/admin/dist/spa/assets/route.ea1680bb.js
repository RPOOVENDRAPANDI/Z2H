import{f as t}from"./index.c822f9b0.js";import{u as a}from"./axios.2c985eff.js";const r=a();var u=t(({router:o})=>{o.beforeEach(async(n,e,s)=>{r.token&&!r.userInfo&&r.getUserInfo(),i(n,e,s)})});const i=(o,n,e)=>{if(!r.token&&o.name!=="sign-in")return e({name:"sign-in"});if(!o.name)return e({name:"sign-in"});e()};export{u as default,i as validateRoutes};