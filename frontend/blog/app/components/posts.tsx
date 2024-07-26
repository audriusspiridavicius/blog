import React from 'react'

type Props = {}

export default async function Posts({}: Props) {
  
    async function getPosts() {
        const res = await fetch(`http://127.0.0.1:8000/posts`)
        const data = await res.json()

        return data
    }

    const posts = await getPosts()

  // Wait for the promises to resolve
    const [postsdata] = await Promise.all([posts])
    return ( 
    <div>
        <div>posts</div>

        {postsdata.map((postt)=>
            <div key={postt.title}>{postt.title}</div>
        )}
    </div>

  )
}