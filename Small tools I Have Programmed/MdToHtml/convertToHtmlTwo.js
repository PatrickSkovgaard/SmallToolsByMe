
//Append html to this string
let html = ""
let check = ""

function convert(text){
    
    let txtArray = text.split("\n")
    let lines = txtArray.length

    for(let i = 0; i < lines-1; i++){
        //console.log("\n\n" + i)
        //console.log(txtArray[i])

        if(txtArray[i][0].localeCompare("#") === 0){
            html += `<h1>` + txtArray[i].split("### ")[1] + `</h1>`
        }
        else{
            console.log("\nELSE !!!!\n\n")
        }
    }
}


//function to insert html tags
function insertHtmlTags(txtArray){

}


let text = "### Root flag\n" 
+
"<br>\n"


convert(text)

console.log(html + "\n\n")

