

function createPost(title, due_date, label,links) {
    
    const data= {
        method: "POST",
        headers: {
            'content-type': "application/json"
        },
        body: JSON.stringify({
        title,due_date,label,links
        })
        
    }
    fetch('https://example.com/api/posts/', data)
    .then(response => response.json())
    .catch(error => console.log(error))
    }


function handleCreated(id, bookmarkInfo) {
  console.log(`New bookmark ID: ${id}`);
  console.log(`New bookmark URL: ${bookmarkInfo.url}`);
  console.log(`New bookmark title: ${bookmarkInfo.title}`);
     alert("BOOKMARK ADDED!");
    var title = bookmarkInfo.title;
    var due_date = new Date();
    var label = "P";
    var links = bookmarkInfo.url;
     createPost(title, due_date, label, links);
}
var browser = browser || chrome;
browser.bookmarks.onChanged.addListener(handleCreated);

