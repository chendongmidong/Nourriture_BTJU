package com.nourriture.app;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.SimpleAdapter;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by liuyifan on 15/12/9.
 */
public class PersonalSettingActivity extends AppCompatActivity {
    private String[] name1 = {"Name", "Account", "Password", "Sex"};
    private int[] picture1 = {R.mipmap.name, R.mipmap.account, R.mipmap.password, R.mipmap.sex};
    private List<Map<String, Object>> listItems1;

    private String[] name2 = {"Country", "Religion"};
    private int[] picture2 = {R.mipmap.country, R.mipmap.religion};
    private List<Map<String, Object>> listItems2;
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.setting);

        listItems1 = new ArrayList<>();
        for(int i = 0; i < name1.length; i++){
            Map<String, Object> listItem = new HashMap<>();
            listItem.put("header",picture1[i]);
            listItem.put("name",name1[i]);
            listItems1.add(listItem);
        }

        ListView list_setting1 = (ListView) findViewById(R.id.list_setting1);
        list_setting1.setAdapter(new SimpleAdapter(this, listItems1, R.layout.setting_item,
                new String[] {"header", "name"},
                new int[] {R.id.header, R.id.name} ));

        list_setting1.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                int position = (int)l;
                //<TODO>
                System.out.println("---Click:" + listItems1.get(position).get("name"));
            }
        });

        listItems2 = new ArrayList<>();
        for(int i = 0; i < name2.length; i++){
            Map<String, Object> listItem = new HashMap<>();
            listItem.put("header",picture2[i]);
            listItem.put("name",name2[i]);
            listItems2.add(listItem);
        }

        ListView list_setting2 = (ListView) findViewById(R.id.list_setting2);
        list_setting2.setAdapter(new SimpleAdapter(this, listItems2, R.layout.setting_item,
                new String[] {"header", "name"},
                new int[] {R.id.header, R.id.name} ));

        list_setting2.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                int position = (int)l;
                //<TODO>
                System.out.println("---Click:" + listItems2.get(position).get("name"));
            }
        });

    }
}
