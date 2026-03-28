from supabase import create_client

class PlayerManager:
    def __init__(self, url: str, key: str):
        self.supabase = create_client(url, key)

    def create_player(self, name, nickname, emoji=None):
        response = self.supabase.table("players").insert({
            "name": name,
            "nickname": nickname,
            "emoji": emoji,
        }).execute()

        if not response.data:
            return None

        return response.data[0]

    def available_players(self):
        response = self.supabase.table("players").select("*").execute()
        players_data = response.data
        return players_data

    def modify_player(self, id_db, nickname, emoji):
        response = (self.supabase.table("players").update({
            "nickname": nickname,
            "emoji": emoji,
        }).eq("id", id_db).execute())

        if not response.data:
            return None

        return response.data[0]

    def get_player_nickname(self, id_db):
        response = self.supabase.table("players").select("*").eq("id", id_db).execute()
        player_nickname = response.data[0]["nickname"]
        return player_nickname

    def get_player_emoji(self, id_db):
        response = self.supabase.table("players").select("*").eq("id", id_db).execute()
        player_emoji = response.data[0]["emoji"]
        return player_emoji