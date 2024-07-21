import{Q as x}from"./QImg.fea902ab.js";import{Q as z}from"./QSelect.84360b9a.js";import{_ as F,r as i,L as G,c as S,w as g,o as $,l as H,m as J,q as s,d as e,n as a,a9 as K,a8 as X,t as Y,M as r,aK as _,A as Z,aa as ee,ab as te}from"./index.18d27cdb.js";import{u as se,Q as oe}from"./QSpinnerFacebook.d84b28a4.js";import{u as le}from"./general.acaf71e2.js";import{i as b}from"./info-circle.abf520f5.js";import{_ as f}from"./CustomTooltip.8a52884a.js";import"./format.c5e89796.js";import"./axios.621c1308.js";const P=w=>(ee("data-v-52280b18"),w=w(),te(),w),ae={class:"row"},ie={class:"col-12"},re={class:"container-height"},de={class:"row q-ml-lg q-pt-lg"},ne={class:""},ue={style:{"font-size":"18px"},class:"text-bold q-pr-md header-text"},ce={class:"q-ml-lg q-mt-sm"},me={class:"row"},ve={class:"q-pt-md"},pe=P(()=>s("span",{class:"text-bold"}," Page Access for different Users ",-1)),xe={class:"q-ml-lg q-mt-sm"},be={class:"row"},fe={class:"col-12 flex items-center justify-start"},ge=P(()=>s("div",{style:{"min-width":"53px"}},"Select Role:",-1)),he={class:"q-ml-sm flex items-center"},_e={style:{"max-width":"300px","min-width":"220px"},class:"q-pa-md"},ye={class:"q-gutter-md"},we={class:"q-ml-lg"},qe={class:"q-ml-lg"},Se={class:"q-ml-lg"},Ce={class:"q-ml-lg"},Pe={class:"q-ml-lg"},Ue={class:"q-ml-lg"},Ve={class:"row no-wrap items-start justify-end"},Re={class:"col-auto row justify-end pr-15"},Ie={__name:"UserSettingsTab",setup(w){const y=le(),h=i("Superadmin"),d=i(!0),n=i(!0),u=i(!0),c=i(!0),m=i(!0),v=i(!0),q=se(),{userRoles:C,userRolePages:U}=G(y),V=i(`
  <div
    class="text-center text-body2 text-white"
    style="border-bottom: 1px solid white; padding-bottom: 0.35rem"
  >
    <b>Web User Settings</b>
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Configuration of information regarding users
    (Admin Level Users). With this data, system
    will allow the user to perform actions across
    web application.
  </div>
`),R=i(`
  <div
    class="text-center text-body2 text-white"
    style="border-bottom: 1px solid white; padding-bottom: 0.35rem"
  >
    <b>Role Based Access</b>
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Configuration of page access against different roles
    in the system.
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Example: Super Admin - All Page Access, Telecaler - Customers
  </div>
`),I=i(`
  <div
    class="text-center text-body2 text-white"
    style="border-bottom: 1px solid white; padding-bottom: 0.35rem"
  >
    <b>Users Page</b>
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Contains personal information and role details of a web user.
    Also can able to add or edit or remove an user from the
    system.
  </div>
`),A=i(`
  <div
    class="text-center text-body2 text-white"
    style="border-bottom: 1px solid white; padding-bottom: 0.35rem"
  >
    <b>Products Page</b>
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Contains Information about products and its prices
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Example: Sony LED TV 44 inches - Rs.64,234/-
  </div>
`),Q=i(`
  <div
    class="text-center text-body2 text-white"
    style="border-bottom: 1px solid white; padding-bottom: 0.35rem"
  >
    <b>Orders Page</b>
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Contains Information about orders booked or purchases
    made by customers (Independent Distributors).
  </div>
`),T=i(`
  <div
    class="text-center text-body2 text-white"
    style="border-bottom: 1px solid white; padding-bottom: 0.35rem"
  >
    <b>Customers Page</b>
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Contains Information about customers(Independent Distributors).
    Their personal info, plan details etc.,
  </div>
`),k=i(`
  <div
    class="text-center text-body2 text-white"
    style="border-bottom: 1px solid white; padding-bottom: 0.35rem"
  >
    <b>Reports Page</b>
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Different types of reports with respect to different
    business use cases. Can able to generate report and
    export an excel file.
  </div>
  <div class="q-mt-sm q-pl-md text-body2 text-white">
    Example:
  </div>
  <div class="text-body2 text-white">
    <ul>
      <li>Purchases made by customer within a certain period</li>
      <li>GST Report for an Auditors</li>
      <li>Customer Joining Report for a Telecaler</li>
    </ul>
  </div>
`),W=i(`
  <div
    class="text-center text-body2 text-white"
    style="border-bottom: 1px solid white; padding-bottom: 0.35rem"
  >
    <b>Settings Page</b>
  </div>
  <div class="q-pl-md q-py-sm text-body2 text-white">
    Has a control over the entire application configurations.
  </div>
  <div class="q-mt-sm q-pl-md text-body2 text-white">
    Example:
  </div>
  <div class="text-body2 text-white">
    <ul>
      <li>Web User Settings Configurations</li>
      <li>Mobile Users Settings Configurations</li>
    </ul>
  </div>
`),E=S(()=>C.value.map(o=>o.name)),p=S(()=>h.value==="Superadmin"),L=S(()=>p.value?!0:!(d.value||n.value||u.value||c.value||m.value||v.value));g(d,o=>{p.value&&(d.value=!0)}),g(n,o=>{p.value&&(n.value=!0)}),g(u,o=>{p.value&&(u.value=!0)}),g(c,o=>{p.value&&(c.value=!0)}),g(m,o=>{p.value&&(m.value=!0)}),g(v,o=>{p.value&&(v.value=!0)}),g(h,o=>{if(o==="Superadmin"){d.value=!0,n.value=!0,u.value=!0,c.value=!0,m.value=!0,v.value=!0;return}N()});const B=()=>{q.loading.show({spinner:oe,spinnerColor:"light-blue",messageColor:"white",backgroundColor:"light-blue",message:""})},j=()=>{q.loading.hide()},D=()=>C.value.find(t=>t.name==h.value).uid,M=()=>{d.value=!1,n.value=!1,u.value=!1,c.value=!1,m.value=!1,v.value=!1},N=()=>{M();let o=U.value.filter(t=>t.role_name===h.value&&t.is_active).map(t=>t.web_page_name);o.includes("users")&&(d.value=!0),o.includes("products")&&(n.value=!0),o.includes("orders")&&(u.value=!0),o.includes("customers")&&(c.value=!0),o.includes("reports")&&(m.value=!0),o.includes("settings")&&(v.value=!0)},O=()=>{if(p.value)return;B();let o={systemRoleUid:D(),users:d.value,products:n.value,orders:u.value,customers:c.value,reports:m.value,settings:v.value};y.saveUserSettings(o).then(t=>{var l;((l=t.data)==null?void 0:l.status)==="success"&&(y.getWebUserRolePages(),q.notify({message:"User Settings Updated Successfully!!!",type:"positive",position:"top"}))}).catch(t=>{q.notify({message:"Something went Wrong. Please contact your admin!!!",type:"negative",position:"top"})}).finally(()=>{j()})};return $(()=>{y.getWebUserRoles(),y.getWebUserRolePages()}),(o,t)=>(H(),J("div",ae,[s("div",ie,[e(K,{class:"card-size h-100vh"},{default:a(()=>[s("div",re,[s("div",de,[s("div",ne,[s("div",ue,[Y(" User Settings "),e(x,{style:{width:"1.2rem"},class:"cursor-pointer q-mx-xs",src:r(b)},{default:a(()=>[e(f,{content:V.value,"max-width":"20rem"},null,8,["content"])]),_:1},8,["src"])]),s("div",ce,[s("div",me,[s("div",ve,[pe,e(x,{style:{width:"1.2rem"},class:"cursor-pointer q-mx-xs",src:r(b)},{default:a(()=>[e(f,{content:R.value,"max-width":"24rem"},null,8,["content"])]),_:1},8,["src"]),s("div",xe,[s("div",be,[s("div",fe,[ge,s("div",he,[s("div",_e,[s("div",ye,[e(z,{filled:"",modelValue:h.value,"onUpdate:modelValue":t[0]||(t[0]=l=>h.value=l),options:r(E)},null,8,["modelValue","options"])])])])])]),s("div",we,[e(_,{modelValue:d.value,"onUpdate:modelValue":t[1]||(t[1]=l=>d.value=l),label:"Users"},{default:a(()=>[e(x,{style:{width:"1.2rem"},class:"cursor-pointer q-mx-xs",src:r(b)},{default:a(()=>[e(f,{content:I.value,"max-width":"20rem"},null,8,["content"])]),_:1},8,["src"])]),_:1},8,["modelValue"])]),s("div",qe,[e(_,{modelValue:n.value,"onUpdate:modelValue":t[2]||(t[2]=l=>n.value=l),label:"Products"},{default:a(()=>[e(x,{style:{width:"1.2rem"},class:"cursor-pointer q-mx-xs",src:r(b)},{default:a(()=>[e(f,{content:A.value,"max-width":"20rem"},null,8,["content"])]),_:1},8,["src"])]),_:1},8,["modelValue"])]),s("div",Se,[e(_,{modelValue:u.value,"onUpdate:modelValue":t[3]||(t[3]=l=>u.value=l),label:"Orders"},{default:a(()=>[e(x,{style:{width:"1.2rem"},class:"cursor-pointer q-mx-xs",src:r(b)},{default:a(()=>[e(f,{content:Q.value,"max-width":"20rem"},null,8,["content"])]),_:1},8,["src"])]),_:1},8,["modelValue"])]),s("div",Ce,[e(_,{modelValue:c.value,"onUpdate:modelValue":t[4]||(t[4]=l=>c.value=l),label:"Customers"},{default:a(()=>[e(x,{style:{width:"1.2rem"},class:"cursor-pointer q-mx-xs",src:r(b)},{default:a(()=>[e(f,{content:T.value,"max-width":"20rem"},null,8,["content"])]),_:1},8,["src"])]),_:1},8,["modelValue"])]),s("div",Pe,[e(_,{modelValue:m.value,"onUpdate:modelValue":t[5]||(t[5]=l=>m.value=l),label:"Reports"},{default:a(()=>[e(x,{style:{width:"1.2rem"},class:"cursor-pointer q-mx-xs",src:r(b)},{default:a(()=>[e(f,{content:k.value,"max-width":"20rem"},null,8,["content"])]),_:1},8,["src"])]),_:1},8,["modelValue"])]),s("div",Ue,[e(_,{modelValue:v.value,"onUpdate:modelValue":t[6]||(t[6]=l=>v.value=l),label:"Settings"},{default:a(()=>[e(x,{style:{width:"1.2rem"},class:"cursor-pointer q-mx-xs",src:r(b)},{default:a(()=>[e(f,{content:W.value,"max-width":"20rem"},null,8,["content"])]),_:1},8,["src"])]),_:1},8,["modelValue"])])])])])])])])])]),_:1}),e(X,{class:"flex justify-end fixed-table-bottom"},{default:a(()=>[s("div",Ve,[s("div",Re,[e(Z,{color:"primary",label:"Save",class:"q-ml-md",disable:r(L),onClick:O},null,8,["disable"])])])]),_:1})])]))}};var De=F(Ie,[["__scopeId","data-v-52280b18"]]);export{De as default};
