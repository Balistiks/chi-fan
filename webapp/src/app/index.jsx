import * as React from 'react';
import {Suspense} from "react";
import {createBrowserRouter, RouterProvider} from "react-router";
import {IndexPage} from "../pages/index-page";
import './styles/normalizez.scss'
import './styles/reset.scss'
import './styles/fonts.scss'
import {Header} from "../widgets/header";

const router = createBrowserRouter([
  {
    path: '/',
    element: <IndexPage />
  }
])

const App = () => {
  return (
    <>
      <Header />
      <Suspense fallback={<p>Загрузка...</p>}>
        <RouterProvider router={router} />
      </Suspense>
    </>
  )
}

export default App;
