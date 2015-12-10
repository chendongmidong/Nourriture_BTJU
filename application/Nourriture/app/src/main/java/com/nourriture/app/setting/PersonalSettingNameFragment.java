package com.nourriture.app.setting;


import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import com.nourriture.app.R;

/**
 * Created by liuyifan on 15/12/10.
 */
public class PersonalSettingNameFragment extends Fragment {
    private View view;
    private String name = "";

    @Override
    public void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);

        if(getArguments()!=null && getArguments().containsKey("name")){
            name = getArguments().getString("name");
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        view = inflater.inflate(R.layout.setting_name_frag, container, false);

        if(!name.equals("")){
            setName(name);
        }
        return view;
    }

    public void setName(String string){
        EditText nameView = (EditText) view.findViewById(R.id.edit_name);
        nameView.setText(string);
    }
}
