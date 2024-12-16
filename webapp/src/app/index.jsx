import * as React from 'react';
import {Suspense} from "react";
import {createBrowserRouter, RouterProvider} from "react-router";
import {IndexPage} from "../pages/index-page";
import './styles/normalizez.scss'
import './styles/reset.scss'

const router = createBrowserRouter([
  {
    path: '/',
    element: <IndexPage />
  }
])

const App = () => {
  return (
    <>
      <Suspense fallback={<p>Загрузка...</p>}>
        <RouterProvider router={router} />
      </Suspense>
    </>
  )
}

export default App;
