import{B as P,i as b,G as d,c as Q,h as S,E as L,g as F,J as q,ae as V,_ as k,bF as I,r as w,l as $,v as B,n as s,d as t,a9 as z,z as U,M as H,a8 as h,bG as M,aM as C,q as g,A as j,aa as A,ab as G}from"./index.c822f9b0.js";import{Q as K}from"./QForm.5279d460.js";import{Q as N,a as W}from"./QLayout.d2d8ff79.js";import{u as E,Q as J}from"./QSpinnerFacebook.173d39e4.js";import{u as D}from"./axios.2c985eff.js";import"./QScrollObserver.88406e47.js";import"./QResizeObserver.230413fd.js";var O=P({name:"QPage",props:{padding:Boolean,styleFn:Function},setup(l,{slots:m}){const{proxy:{$q:r}}=F(),a=b(q,d);if(a===d)return console.error("QPage needs to be a deep child of QLayout"),d;if(b(V,d)===d)return console.error("QPage needs to be child of QPageContainer"),d;const u=Q(()=>{const i=(a.header.space===!0?a.header.size:0)+(a.footer.space===!0?a.footer.size:0);if(typeof l.styleFn=="function"){const _=a.isContainer.value===!0?a.containerHeight.value:r.screen.height;return l.styleFn(i,_)}return{minHeight:a.isContainer.value===!0?a.containerHeight.value-i+"px":r.screen.height===0?i!==0?`calc(100vh - ${i}px)`:"100vh":r.screen.height-i+"px"}}),f=Q(()=>`q-page${l.padding===!0?" q-layout-padding":""}`);return()=>S("main",{class:f.value,style:u.value},L(m.default))}});const x=l=>(A("data-v-6b155434"),l=l(),G(),l),T=x(()=>g("img",{src:"static/company_logo_V2.png",alt:""},null,-1)),X=x(()=>g("div",{class:"text-center q-pt-lg"},[g("div",{class:"col text-h6 ellipsis"},"Log in")],-1)),Y={class:"row justify-center"},Z={__name:"LoginPage",setup(l){const m=I(),r=D(),a=w(""),p=w(""),u=E(),f=()=>{u.loading.show({spinner:J,spinnerColor:"light-blue",messageColor:"white",backgroundColor:"light-blue",message:""})},i=()=>{u.loading.hide()},_=()=>{f();let y={email:a.value,password:p.value,accessed_from:"web"};r.userLoginWithPassword(y).then(n=>{let e=n.data.token;r.token=e,localStorage.setItem("token",e),r.getUserInfo(),m.push({name:"main"})}).catch(n=>{var v;let e=null,c=null,o=(v=n.response)==null?void 0:v.data;o!=null&&o.non_field_errors?(e=o.non_field_errors,c=e[0]):o!=null&&o.email?(e=o.email,c=e[0]):o||(c="Something went Wrong. Please contact your admin!!!"),c&&u.notify({message:c,type:"negative",position:"top"})}).finally(()=>{i()})};return(y,n)=>($(),B(N,null,{default:s(()=>[t(W,null,{default:s(()=>[t(O,{class:"flex bg-image flex-center"},{default:s(()=>[t(z,{style:U(H(u).screen.lt.sm?{width:"80%"}:{width:"30%"})},{default:s(()=>[t(h,null,{default:s(()=>[t(M,{size:"103px",class:"absolute-center shadow-10"},{default:s(()=>[T]),_:1})]),_:1}),t(h,null,{default:s(()=>[X]),_:1}),t(h,null,{default:s(()=>[t(K,{class:"q-gutter-md",onSubmit:_},{default:s(()=>[t(C,{autofocus:"",outlined:"",modelValue:a.value,"onUpdate:modelValue":n[0]||(n[0]=e=>a.value=e),"bg-color":"grey-3",label:"email",type:"email",rules:[e=>!!e||"Field is required"],"no-error-icon":""},null,8,["modelValue","rules"]),t(C,{type:"password",outlined:"",modelValue:p.value,"onUpdate:modelValue":n[1]||(n[1]=e=>p.value=e),"bg-color":"grey-3",label:"Password",rules:[e=>!!e||"Field is required"],"no-error-icon":""},null,8,["modelValue","rules"]),g("div",Y,[t(j,{label:"Login",type:"submit",color:"primary"})])]),_:1})]),_:1})]),_:1},8,["style"])]),_:1})]),_:1})]),_:1}))}};var ne=k(Z,[["__scopeId","data-v-6b155434"]]);export{ne as default};
