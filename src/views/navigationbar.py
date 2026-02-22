import flet as ft

class NavigationBar(ft.NavigationBar):
    def __init__(self, page: ft.Page | None = None, selected_index: int = 1, light: bool | None = None):
    
        if light is None and page is not None:
            light = page.theme_mode == ft.ThemeMode.LIGHT

            on_change = self._change_view if page is not None else None

            bgcolor = ft.Colors.WHITE if light else ft.Colors.BLACK
            icon_color = ft.Colors.BLACK if light else ft.Colors.WHITE
        
        super().__init__(
            selected_index=selected_index,
            destinations=[
                ft.NavigationBarDestination(
                    icon=(ft.Icon(ft.Icons.HOME_OUTLINED, color=icon_color) if light else ft.Icons.HOME_OUTLINED),
                    selected_icon=(ft.Icon(ft.Icons.HOME, color=icon_color) if light else ft.Icons.HOME),
                    label="Inicio"
                ),
                ft.NavigationBarDestination(
                    icon=(ft.Icon(ft.Icons.SEARCH_OUTLINED, color=icon_color) if light else ft.Icons.SEARCH_OUTLINED),
                    selected_icon=(ft.Icon(ft.Icons.SEARCH, color=icon_color) if light else ft.Icons.SEARCH),
                    label="Buscar"
                ),
                ft.NavigationBarDestination(
                    icon=(ft.Icon(ft.Icons.PLAYLIST_PLAY_OUTLINED, color=icon_color) if light else ft.Icons.PLAYLIST_PLAY_OUTLINED),
                    selected_icon=(ft.Icon(ft.Icons.PLAYLIST_PLAY, color=icon_color) if light else ft.Icons.PLAYLIST_PLAY),
                    label="Playlist"
                ),
                ft.NavigationBarDestination(
                    icon=(ft.Icon(ft.Icons.DASHBOARD_OUTLINED, color=icon_color) if light else ft.Icons.DASHBOARD_OUTLINED),
                    selected_icon=(ft.Icon(ft.Icons.DASHBOARD, color=icon_color) if light else ft.Icons.DASHBOARD),
                    label="Más"
                ),
            ],
            on_change=on_change,
            bgcolor=bgcolor,
        )

    def _change_view(self, e: ft.ControlEvent):
        page = e.page
        selected_index = e.control.selected_index
        page.controls.clear()

        from .homeview import HomeView
        from .searchview import SearchView
        from .playlistview import PlaylistView
        from .moreview import MoreView

        if selected_index == 0:
            page.add(HomeView(page))
        elif selected_index == 1:
            page.add(SearchView(page))
        elif selected_index == 2:
            page.add(PlaylistView(page))
        elif selected_index == 3:
            page.add(MoreView(page))

        page.add(NavigationBar(page=page, selected_index=selected_index, light=(page.theme_mode == ft.ThemeMode.LIGHT)))
        page.update()