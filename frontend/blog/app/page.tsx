import Image from "next/image";
import Posts from "./components/posts";

export default function Home() {

  // async function getArtist(username: string) {
  //   const res = await fetch(`https://api.example.com/artist/${username}`)
  //   return res.json()
  // }
   
  // async function getArtistAlbums(username: string) {
  //   const res = await fetch(`https://api.example.com/artist/${username}/albums`)
  //   return res.json()
  // }

  return (
    <>
    <div>
      <div className="">
        
        <div className="flex">
          <div className="w-3/12 border border-black mr-5"></div>
          <div className="w-9/12 border border-red-400 text-center">
            <Posts/>
          </div>
        </div>

      </div>
    </div>
   
    </>
  );
}
